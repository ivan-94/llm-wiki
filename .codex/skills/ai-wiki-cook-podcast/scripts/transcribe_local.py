#!/usr/bin/env python3
"""Transcribe a downloaded podcast audio file with local open-source Whisper."""

from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import urlretrieve


WIKI_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_MODEL = "base"
DEFAULT_HOTWORDS_FILE = WIKI_ROOT / "docs" / ".hotword.md"
DEFAULT_WHISPER_CPP_MODEL_DIR = Path.home() / ".cache" / "whisper.cpp"
DEFAULT_WHISPER_CPP_MODEL_SOURCES = [
    "https://modelscope.cn/models/iceCream2025/whisper.cpp/resolve/master/ggml-{model}.bin",
    "https://modelscope.cn/models/cjc1887415157/whisper.cpp/resolve/master/ggml-{model}.bin",
    "https://hf-mirror.com/ggerganov/whisper.cpp/resolve/main/ggml-{model}.bin",
    "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-{model}.bin",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audio", help="Audio file to transcribe")
    parser.add_argument("--cache-dir", default=None, help="Directory for transcript outputs")
    parser.add_argument(
        "--engine",
        choices=("auto", "openai-whisper", "whisper-cpp"),
        default="auto",
        help="Transcription engine. auto prefers whisper.cpp when configured, then openai-whisper.",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Whisper model name")
    parser.add_argument("--language", default="auto", help="Whisper language; use auto for auto-detection")
    parser.add_argument("--device", default="auto", help="Whisper device: auto, cpu, cuda, or mps")
    parser.add_argument("--threads", type=int, default=0, help="Torch CPU thread count; 0 keeps Whisper default")
    parser.add_argument("--initial-prompt", default="", help="Prompt text to bias transcription spelling/terms")
    parser.add_argument("--initial-prompt-file", default=None, help="UTF-8 file with episode-specific prompt text")
    parser.add_argument(
        "--hotwords-file",
        default=str(DEFAULT_HOTWORDS_FILE),
        help="UTF-8 Markdown/text hotwords file; defaults to docs/.hotword.md when present",
    )
    parser.add_argument("--no-hotwords", action="store_true", help="Do not load repository hotwords")
    parser.add_argument("--whisper-cpp-bin", default=None, help="Path to whisper.cpp whisper-cli")
    parser.add_argument("--whisper-cpp-model", default=None, help="Path to a whisper.cpp ggml model file")
    parser.add_argument(
        "--whisper-cpp-model-dir",
        default=str(DEFAULT_WHISPER_CPP_MODEL_DIR),
        help="Directory containing ggml-<model>.bin files for whisper.cpp",
    )
    parser.add_argument(
        "--whisper-cpp-model-source",
        action="append",
        default=None,
        help=(
            "Model URL template or direct URL for whisper.cpp model download. "
            "Use {model} for the ggml model name. Can be repeated."
        ),
    )
    parser.add_argument("--no-install", action="store_true", help="Do not install missing local tools or models")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args()


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=True, text=True, capture_output=True)


def common_bin_paths(name: str) -> list[Path]:
    home = Path.home()
    return [
        home / ".local" / "bin" / name,
        home / ".cargo" / "bin" / name,
        home / ".rye" / "shims" / name,
    ]


def find_executable(name: str) -> str | None:
    found = shutil.which(name)
    if found:
        return found
    for path in common_bin_paths(name):
        if path.exists() and path.is_file():
            return str(path)
    return None


def python_from_shebang(executable: str) -> str | None:
    try:
        first_line = Path(executable).read_text(encoding="utf-8", errors="ignore").splitlines()[0]
    except (IndexError, OSError):
        return None
    if not first_line.startswith("#!"):
        return None
    command = shlex.split(first_line[2:].strip())
    if not command:
        return None
    if Path(command[0]).name == "env" and len(command) > 1:
        return shutil.which(command[1])
    return command[0]


def install_openai_whisper() -> None:
    uv = find_executable("uv")
    if uv:
        subprocess.run([uv, "tool", "install", "--upgrade", "openai-whisper"], check=True)
        return
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--user", "-U", "openai-whisper"], check=True)
    except subprocess.CalledProcessError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-U", "openai-whisper"], check=True)


def install_whisper_cpp() -> None:
    brew = find_executable("brew")
    if not brew:
        raise SystemExit("Missing whisper.cpp and Homebrew is unavailable. Install `whisper-cpp` and rerun.")
    subprocess.run([brew, "install", "whisper-cpp"], check=True)


def ensure_whisper(no_install: bool) -> str:
    whisper = find_executable("whisper")
    if whisper:
        return whisper
    if no_install:
        raise SystemExit("Missing local `whisper` CLI and --no-install was provided.")
    install_openai_whisper()
    whisper = find_executable("whisper")
    if whisper:
        return whisper
    raise SystemExit(
        "Installed openai-whisper but still cannot find `whisper` on PATH. "
        "Check ~/.local/bin or the uv tool install directory."
    )


def find_whisper_cpp(explicit: str | None = None) -> str | None:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        return str(path) if path.is_file() else None
    for name in ("whisper-cli", "whisper-cpp"):
        found = find_executable(name)
        if found:
            return found
    return None


def ensure_whisper_cpp(args: argparse.Namespace) -> tuple[str, bool]:
    whisper_cpp = find_whisper_cpp(args.whisper_cpp_bin)
    installed = False
    if whisper_cpp:
        return whisper_cpp, installed
    if args.no_install:
        raise SystemExit("Missing whisper.cpp `whisper-cli` and --no-install was provided.")
    install_whisper_cpp()
    installed = True
    whisper_cpp = find_whisper_cpp(args.whisper_cpp_bin)
    if whisper_cpp:
        return whisper_cpp, installed
    raise SystemExit("Installed whisper.cpp but still cannot find `whisper-cli` or `whisper-cpp` on PATH.")


def whisper_cpp_model_name(model: str) -> str:
    aliases = {
        "large": "large-v3",
        "turbo": "large-v3-turbo",
    }
    return aliases.get(model, model)


def resolve_whisper_cpp_model(model: str, explicit: str | None, model_dir: str) -> str | None:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        return str(path) if path.is_file() else None
    directory = Path(model_dir).expanduser().resolve()
    candidate = directory / f"ggml-{whisper_cpp_model_name(model)}.bin"
    return str(candidate) if candidate.is_file() else None


def whisper_cpp_model_sources(args: argparse.Namespace) -> list[str]:
    if args.whisper_cpp_model_source:
        return args.whisper_cpp_model_source
    env_sources = os.environ.get("COOK_PODCAST_WHISPER_CPP_MODEL_SOURCES", "").strip()
    if env_sources:
        return [source.strip() for source in env_sources.split(",") if source.strip()]
    return DEFAULT_WHISPER_CPP_MODEL_SOURCES


def model_source_url(source: str, model_name: str) -> str:
    return source.format(model=model_name) if "{model}" in source else source


def download_with_progress(url: str, destination: Path) -> str | None:
    curl = find_executable("curl")
    tmp = destination.with_suffix(destination.suffix + ".tmp")
    if tmp.exists():
        tmp.unlink()
    try:
        if curl:
            subprocess.run(
                [
                    curl,
                    "-L",
                    "--fail",
                    "--retry",
                    "3",
                    "--retry-delay",
                    "2",
                    "--connect-timeout",
                    "20",
                    "--progress-bar",
                    "-o",
                    str(tmp),
                    url,
                ],
                check=True,
            )
        else:
            urlretrieve(url, tmp)
    except (subprocess.CalledProcessError, URLError, OSError) as error:
        if tmp.exists():
            tmp.unlink()
        return str(error)
    if not tmp.exists() or tmp.stat().st_size < 1_000_000:
        if tmp.exists():
            tmp.unlink()
        return "downloaded file is unexpectedly small"
    tmp.rename(destination)
    return None


def ensure_whisper_cpp_model(args: argparse.Namespace) -> tuple[str, bool, str | None]:
    model_path = resolve_whisper_cpp_model(args.model, args.whisper_cpp_model, args.whisper_cpp_model_dir)
    if model_path:
        return model_path, False, None
    if args.whisper_cpp_model:
        raise SystemExit(f"whisper.cpp model file does not exist: {args.whisper_cpp_model}")
    if args.no_install:
        raise SystemExit("Missing whisper.cpp ggml model file and --no-install was provided.")
    model_name = whisper_cpp_model_name(args.model)
    destination_dir = Path(args.whisper_cpp_model_dir).expanduser().resolve()
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / f"ggml-{model_name}.bin"
    failures: list[str] = []
    for source in whisper_cpp_model_sources(args):
        url = model_source_url(source, model_name)
        error = download_with_progress(url, destination)
        if error is None:
            return str(destination), True, url
        failures.append(f"{url}: {error}")
    raise SystemExit("Failed to download whisper.cpp model from all configured sources:\n" + "\n".join(failures))


def choose_engine(args: argparse.Namespace) -> str:
    if args.engine != "auto":
        return args.engine
    whisper_cpp = find_whisper_cpp(args.whisper_cpp_bin)
    whisper_cpp_model = resolve_whisper_cpp_model(args.model, args.whisper_cpp_model, args.whisper_cpp_model_dir)
    if whisper_cpp and whisper_cpp_model:
        return "whisper-cpp"
    return "openai-whisper"


def whisper_cpp_language(language: str) -> str:
    normalized = language.strip().lower()
    if normalized in {"", "auto"}:
        return "auto"
    language_map = {
        "english": "en",
        "en": "en",
        "chinese": "zh",
        "zh": "zh",
        "zh-cn": "zh",
        "mandarin": "zh",
        "japanese": "ja",
        "ja": "ja",
        "korean": "ko",
        "ko": "ko",
    }
    return language_map.get(normalized, language)


def ensure_ffmpeg(no_install: bool) -> None:
    if find_executable("ffmpeg"):
        return
    if no_install:
        raise SystemExit("Missing `ffmpeg` and --no-install was provided.")
    brew = find_executable("brew")
    if brew:
        subprocess.run([brew, "install", "ffmpeg"], check=True)
        return
    raise SystemExit("Missing `ffmpeg`, which Whisper requires. Install ffmpeg and rerun transcription.")


def whisper_cpp_audio_path(audio: Path, cache_dir: Path, no_install: bool) -> tuple[Path, bool]:
    if audio.suffix.lower() in {".flac", ".mp3", ".ogg", ".wav"}:
        return audio, False
    ensure_ffmpeg(no_install)
    converted = cache_dir / f"{audio.stem}.whisper-cpp.wav"
    command = [
        find_executable("ffmpeg") or "ffmpeg",
        "-y",
        "-i",
        str(audio),
        "-ar",
        "16000",
        "-ac",
        "1",
        "-c:a",
        "pcm_s16le",
        str(converted),
    ]
    subprocess.run(command, check=True)
    return converted, True


def detect_device(whisper: str, requested: str) -> str:
    requested = requested.strip().lower()
    if requested and requested != "auto":
        return requested
    python = python_from_shebang(whisper) or sys.executable
    code = """
import json
try:
    import torch
    payload = {
        "mps": bool(getattr(torch.backends, "mps", None) and torch.backends.mps.is_available()),
        "cuda": bool(torch.cuda.is_available()),
    }
except Exception:
    payload = {"mps": False, "cuda": False}
print(json.dumps(payload))
"""
    try:
        result = subprocess.run([python, "-c", code], check=True, text=True, capture_output=True)
        payload = json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError):
        payload = {"mps": False, "cuda": False}
    if payload.get("cuda"):
        return "cuda"
    if payload.get("mps"):
        return "mps"
    return "cpu"


def normalize_hotword_line(line: str, *, require_item_prefix: bool) -> list[str]:
    stripped = line.strip()
    if not stripped or stripped.startswith("#") or stripped.startswith(">"):
        return []
    if stripped.startswith("```"):
        return []
    has_item_prefix = False
    prefixes = ("- [ ]", "- [x]", "- ", "* ", "+ ")
    for prefix in prefixes:
        if stripped.lower().startswith(prefix):
            stripped = stripped[len(prefix) :].strip()
            has_item_prefix = True
            break
    stripped, had_number_prefix = strip_numbered_prefix(stripped)
    has_item_prefix = has_item_prefix or had_number_prefix
    if require_item_prefix and not has_item_prefix:
        return []
    if not stripped or stripped.startswith("#"):
        return []
    if "`" in stripped:
        stripped = stripped.replace("`", "")
    if "|" in stripped and stripped.startswith("[[") and stripped.endswith("]]"):
        stripped = stripped[2:-2].split("|", 1)[-1]
    elif stripped.startswith("[[") and stripped.endswith("]]"):
        stripped = stripped[2:-2]
    for marker in ("：", ":", " - ", " — "):
        if marker in stripped:
            left, right = stripped.split(marker, 1)
            if len(left) <= 12 and right.strip():
                stripped = right.strip()
                break
    parts = [part.strip() for part in stripped.replace("，", ",").replace("、", ",").split(",")]
    return [part for part in parts if part]


def strip_numbered_prefix(value: str) -> tuple[str, bool]:
    index = 0
    while index < len(value) and value[index].isdigit():
        index += 1
    if index and index < len(value) and value[index] in {".", "、", ")"}:
        return value[index + 1 :].strip(), True
    return value, False


def read_hotwords(path: str | None, *, default_path: Path = DEFAULT_HOTWORDS_FILE) -> list[str]:
    if not path:
        return []
    hotwords_path = Path(path).expanduser().resolve()
    if not hotwords_path.is_file():
        if hotwords_path == default_path.resolve():
            return []
        raise SystemExit(f"Hotwords file does not exist: {hotwords_path}")
    words: list[str] = []
    in_code_fence = False
    lines = hotwords_path.read_text(encoding="utf-8").splitlines()
    has_markers = any("hotwords:start" in line for line in lines)
    in_hotwords = not has_markers
    for line in lines:
        lowered = line.lower()
        if "hotwords:start" in lowered:
            in_hotwords = True
            continue
        if "hotwords:end" in lowered:
            in_hotwords = False
            continue
        if line.strip().startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence or not in_hotwords:
            continue
        words.extend(normalize_hotword_line(line, require_item_prefix=not has_markers))
    seen: set[str] = set()
    unique: list[str] = []
    for word in words:
        if word not in seen:
            seen.add(word)
            unique.append(word)
    return unique


def read_initial_prompt_file(path: str | None) -> str:
    if not path:
        return ""
    prompt_path = Path(path).expanduser().resolve()
    if not prompt_path.is_file():
        raise SystemExit(f"Initial prompt file does not exist: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8").strip()


def build_initial_prompt(initial_prompt: str, initial_prompt_file: str, hotwords: list[str]) -> str:
    pieces: list[str] = []
    if initial_prompt_file:
        pieces.append(initial_prompt_file)
    if initial_prompt.strip():
        pieces.append(initial_prompt.strip())
    if hotwords:
        pieces.append("以下术语可能出现在音频中，请优先按这些写法转写：" + "、".join(hotwords))
    return "\n".join(pieces).strip()


def write_used_prompt(cache_dir: Path, prompt: str) -> Path | None:
    if not prompt:
        return None
    path = cache_dir / "transcription-prompt.txt"
    path.write_text(prompt, encoding="utf-8")
    return path


def model_cache_candidates(model: str) -> list[Path]:
    cache = Path.home() / ".cache" / "whisper"
    aliases = {
        "large": "large-v3",
        "turbo": "large-v3-turbo",
    }
    names = [model, aliases.get(model, "")]
    candidates: list[Path] = []
    for name in names:
        if name:
            candidates.append(cache / f"{name}.pt")
    return candidates


def quarantine_model_cache(model: str) -> list[str]:
    moved: list[str] = []
    suffix = datetime.now().strftime("%Y%m%d-%H%M%S")
    for candidate in model_cache_candidates(model):
        if candidate.exists():
            destination = candidate.with_name(f"{candidate.name}.corrupt-{suffix}")
            candidate.rename(destination)
            moved.append(str(destination))
    return moved


def checksum_failed(result: subprocess.CompletedProcess[str]) -> bool:
    output = f"{result.stdout}\n{result.stderr}".lower()
    return "checksum" in output or "sha256" in output or "does not match" in output


def run_whisper(command: list[str], model: str) -> subprocess.CompletedProcess[str]:
    first = subprocess.run(command, text=True, capture_output=True)
    if first.returncode == 0:
        return first
    if checksum_failed(first):
        moved = quarantine_model_cache(model)
        if moved:
            print(f"Whisper model checksum failed; quarantined cache file(s): {moved}", file=sys.stderr)
        retry = subprocess.run(command, text=True, capture_output=True)
        if retry.returncode == 0:
            return retry
        print(retry.stdout, end="")
        print(retry.stderr, end="", file=sys.stderr)
        raise SystemExit(retry.returncode)
    print(first.stdout, end="")
    print(first.stderr, end="", file=sys.stderr)
    raise SystemExit(first.returncode)


def timestamp(seconds: float) -> str:
    total_seconds = int(seconds)
    hours, rem = divmod(total_seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def transcript_markdown(transcript: dict[str, Any]) -> str:
    lines: list[str] = []
    segments = transcript.get("segments")
    if isinstance(segments, list):
        for segment in segments:
            if not isinstance(segment, dict):
                continue
            start = float(segment.get("start") or 0)
            end = float(segment.get("end") or start)
            body = str(segment.get("text") or "").strip()
            if body:
                lines.append(f"[{timestamp(start)} {timestamp(end)}] {body}")
    if not lines:
        text = str(transcript.get("text") or "").strip()
        if text:
            lines.append(text)
    return "\n".join(lines)


def nested_number(payload: dict[str, Any], *path: str) -> float | None:
    current: Any = payload
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    if isinstance(current, (int, float)):
        return float(current)
    return None


def whisper_cpp_segments(raw: dict[str, Any]) -> list[dict[str, Any]]:
    candidates = raw.get("transcription") or raw.get("segments") or []
    if not isinstance(candidates, list):
        return []
    segments: list[dict[str, Any]] = []
    for item in candidates:
        if not isinstance(item, dict):
            continue
        body = str(item.get("text") or item.get("transcript") or "").strip()
        if not body:
            continue
        start = (
            nested_number(item, "start")
            or nested_number(item, "t0")
            or nested_number(item, "offsets", "from")
            or 0.0
        )
        end = nested_number(item, "end") or nested_number(item, "t1") or nested_number(item, "offsets", "to") or start
        if start > 1000 or end > 1000:
            start /= 1000
            end /= 1000
        segments.append({"start": start, "end": end, "text": body})
    return segments


def normalized_whisper_cpp_transcript(raw: dict[str, Any], txt: str) -> dict[str, Any]:
    text = txt.strip() or str(raw.get("text") or "").strip()
    segments = whisper_cpp_segments(raw)
    if not text and segments:
        text = "\n".join(str(segment["text"]).strip() for segment in segments if segment.get("text"))
    return {
        "text": text,
        "segments": segments,
        "raw_whisper_cpp": raw,
    }


def load_whisper_cpp_output(prefix: Path) -> dict[str, Any]:
    json_path = prefix.with_suffix(".json")
    txt_path = prefix.with_suffix(".txt")
    if not json_path.exists() and not txt_path.exists():
        raise SystemExit("whisper.cpp finished but no JSON or TXT transcript was found.")
    raw: dict[str, Any] = {}
    if json_path.exists():
        raw = json.loads(json_path.read_text(encoding="utf-8"))
    txt = txt_path.read_text(encoding="utf-8") if txt_path.exists() else ""
    return normalized_whisper_cpp_transcript(raw, txt)


def transcribe_with_whisper_cpp(
    args: argparse.Namespace,
    audio: Path,
    cache_dir: Path,
    initial_prompt: str,
    hotwords: list[str],
    used_prompt_path: Path | None,
) -> dict[str, Any]:
    whisper_cpp, installed_cli = ensure_whisper_cpp(args)
    model_path, downloaded_model, model_download_source = ensure_whisper_cpp_model(args)
    prepared_audio, converted_audio = whisper_cpp_audio_path(audio, cache_dir, args.no_install)
    output_prefix = cache_dir / "transcript-whisper-cpp"
    command = [
        whisper_cpp,
        "-m",
        model_path,
        "-f",
        str(prepared_audio),
        "-of",
        str(output_prefix),
        "-oj",
        "-otxt",
        "-l",
        whisper_cpp_language(args.language),
    ]
    if args.threads > 0:
        command.extend(["-t", str(args.threads)])
    if args.device.strip().lower() == "cpu":
        command.append("--no-gpu")
    if initial_prompt:
        command.extend(["--prompt", initial_prompt])
    result = subprocess.run(command, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

    transcript = load_whisper_cpp_output(output_prefix)
    transcript_json = cache_dir / "transcript.json"
    transcript_json.write_text(json.dumps(transcript, ensure_ascii=False, indent=2), encoding="utf-8")
    transcript_md = cache_dir / "transcript.md"
    transcript_md.write_text(transcript_markdown(transcript), encoding="utf-8")

    return {
        "engine": "whisper.cpp-local",
        "whisper_command": whisper_cpp,
        "whisper_cpp_installed": installed_cli,
        "whisper_cpp_model": model_path,
        "whisper_cpp_model_downloaded": downloaded_model,
        "whisper_cpp_model_download_source": model_download_source,
        "model": args.model,
        "language": args.language,
        "device": "cpu" if args.device.strip().lower() == "cpu" else "whisper.cpp-auto-gpu",
        "threads": args.threads,
        "hotwords": hotwords,
        "hotwords_file": str(Path(args.hotwords_file).expanduser().resolve()) if args.hotwords_file else None,
        "initial_prompt_file": str(Path(args.initial_prompt_file).expanduser().resolve())
        if args.initial_prompt_file
        else None,
        "transcription_prompt": str(used_prompt_path) if used_prompt_path else None,
        "initial_prompt_used": bool(initial_prompt),
        "audio_path": str(audio),
        "prepared_audio_path": str(prepared_audio),
        "converted_audio_for_whisper_cpp": converted_audio,
        "transcript_json": str(transcript_json),
        "transcript_markdown": str(transcript_md),
        "text_characters": len(str(transcript.get("text") or "")),
        "segments": len(transcript.get("segments") or []),
    }


def transcribe_with_openai_whisper(
    args: argparse.Namespace,
    audio: Path,
    cache_dir: Path,
    initial_prompt: str,
    hotwords: list[str],
    used_prompt_path: Path | None,
) -> dict[str, Any]:
    ensure_ffmpeg(args.no_install)
    whisper = ensure_whisper(args.no_install)
    device = detect_device(whisper, args.device)
    command = [
        whisper,
        str(audio),
        "--model",
        args.model,
        "--device",
        device,
        "--task",
        "transcribe",
        "--output_format",
        "json",
        "--output_dir",
        str(cache_dir),
    ]
    if args.language.strip().lower() not in {"auto", ""}:
        command.extend(["--language", args.language])
    if args.threads > 0:
        command.extend(["--threads", str(args.threads)])
    if initial_prompt:
        command.extend(["--initial_prompt", initial_prompt, "--carry_initial_prompt", "True"])
    result = run_whisper(command, args.model)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)

    generated_json = cache_dir / f"{audio.stem}.json"
    transcript_json = cache_dir / "transcript.json"
    if not generated_json.exists():
        candidates = sorted(cache_dir.glob("*.json"), key=lambda path: path.stat().st_mtime, reverse=True)
        if not candidates:
            raise SystemExit("Whisper finished but no JSON transcript was found.")
        generated_json = candidates[0]
    transcript = json.loads(generated_json.read_text(encoding="utf-8"))
    if generated_json != transcript_json:
        transcript_json.write_text(json.dumps(transcript, ensure_ascii=False, indent=2), encoding="utf-8")
    transcript_md = cache_dir / "transcript.md"
    transcript_md.write_text(transcript_markdown(transcript), encoding="utf-8")

    return {
        "engine": "openai-whisper-local",
        "whisper_command": whisper,
        "model": args.model,
        "language": args.language,
        "device": device,
        "threads": args.threads,
        "hotwords": hotwords,
        "hotwords_file": str(Path(args.hotwords_file).expanduser().resolve()) if args.hotwords_file else None,
        "initial_prompt_file": str(Path(args.initial_prompt_file).expanduser().resolve())
        if args.initial_prompt_file
        else None,
        "transcription_prompt": str(used_prompt_path) if used_prompt_path else None,
        "initial_prompt_used": bool(initial_prompt),
        "audio_path": str(audio),
        "transcript_json": str(transcript_json),
        "transcript_markdown": str(transcript_md),
        "text_characters": len(str(transcript.get("text") or "")),
        "segments": len(transcript.get("segments") or []),
    }


def main() -> None:
    args = parse_args()
    audio = Path(args.audio).expanduser().resolve()
    if not audio.is_file():
        raise SystemExit(f"Audio file does not exist: {audio}")
    cache_dir = Path(args.cache_dir).expanduser().resolve() if args.cache_dir else audio.parent
    cache_dir.mkdir(parents=True, exist_ok=True)

    engine = choose_engine(args)
    hotwords = [] if args.no_hotwords else read_hotwords(args.hotwords_file)
    initial_prompt_file = read_initial_prompt_file(args.initial_prompt_file)
    initial_prompt = build_initial_prompt(args.initial_prompt, initial_prompt_file, hotwords)
    used_prompt_path = write_used_prompt(cache_dir, initial_prompt)
    if engine == "whisper-cpp":
        payload = transcribe_with_whisper_cpp(args, audio, cache_dir, initial_prompt, hotwords, used_prompt_path)
    else:
        payload = transcribe_with_openai_whisper(args, audio, cache_dir, initial_prompt, hotwords, used_prompt_path)
    payload["selected_engine"] = engine
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Transcript: {payload['transcript_markdown']}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
