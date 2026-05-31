#!/usr/bin/env python3
"""Resolve an Apple Podcasts episode URL to metadata and an audio file."""

from __future__ import annotations

import argparse
import json
import mimetypes
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


WIKI_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_CACHE_ROOT = WIKI_ROOT / ".codex" / "cache" / "cook-podcast"
USER_AGENT = "Mozilla/5.0 cook-podcast/0.1"
SUPPORTED_AUDIO_EXTENSIONS = {".mp3", ".m4a", ".aac", ".wav", ".flac", ".ogg", ".opus", ".mp4"}
CONTENT_TYPE_EXTENSIONS = {
    "audio/mpeg": ".mp3",
    "audio/mp3": ".mp3",
    "audio/mp4": ".m4a",
    "audio/x-m4a": ".m4a",
    "audio/aac": ".aac",
    "audio/wav": ".wav",
    "audio/x-wav": ".wav",
    "audio/flac": ".flac",
    "audio/ogg": ".ogg",
    "audio/opus": ".opus",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Apple Podcasts episode URL")
    parser.add_argument("--cache-root", default=str(DEFAULT_CACHE_ROOT), help="Cook podcast cache root")
    parser.add_argument("--download", action="store_true", help="Download the resolved audio into cache")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args()


def request_json(url: str) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def parse_apple_url(url: str) -> dict[str, str]:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    podcast_match = re.search(r"/id(\d+)(?:[/?]|$)", parsed.path)
    if not podcast_match:
        raise SystemExit(f"Could not find podcast id in Apple Podcasts URL: {url}")
    episode_ids = query.get("i", [])
    if not episode_ids:
        raise SystemExit("Apple Podcasts URL must include an episode id query parameter `i=`.")
    storefront = ""
    parts = [part for part in parsed.path.split("/") if part]
    if parts and re.fullmatch(r"[a-z]{2}", parts[0], flags=re.IGNORECASE):
        storefront = parts[0].lower()
    return {
        "input_url": url,
        "podcast_id": podcast_match.group(1),
        "episode_id": episode_ids[0],
        "storefront": storefront,
        "language": query.get("l", [""])[0],
    }


def lookup_urls(podcast_id: str, storefront: str) -> list[str]:
    params = {
        "id": podcast_id,
        "entity": "podcastEpisode",
        "limit": "200",
    }
    countries: list[str | None] = []
    if storefront:
        countries.append(storefront)
    countries.extend([None, "cn", "us"])
    seen: set[str] = set()
    urls: list[str] = []
    for country in countries:
        current = dict(params)
        if country:
            current["country"] = country
        url = f"https://itunes.apple.com/lookup?{urllib.parse.urlencode(current)}"
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def find_episode(parsed_url: dict[str, str]) -> tuple[dict[str, Any], dict[str, Any], str]:
    episode_id = int(parsed_url["episode_id"])
    last_payload: dict[str, Any] | None = None
    for lookup_url in lookup_urls(parsed_url["podcast_id"], parsed_url["storefront"]):
        payload = request_json(lookup_url)
        last_payload = payload
        results = payload.get("results", [])
        podcast = next((item for item in results if item.get("wrapperType") == "track" and item.get("kind") == "podcast"), {})
        episodes = [item for item in results if item.get("wrapperType") == "podcastEpisode"]
        match = next((item for item in episodes if int(item.get("trackId", -1)) == episode_id), None)
        if match:
            return podcast, match, lookup_url
    sample_ids: list[int] = []
    if last_payload:
        sample_ids = [
            int(item["trackId"])
            for item in last_payload.get("results", [])
            if item.get("wrapperType") == "podcastEpisode" and "trackId" in item
        ][:10]
    raise SystemExit(
        "Could not find the episode in Apple lookup results. "
        f"Episode id: {episode_id}. Sample episode ids: {sample_ids}. "
        "Use browser capture fallback."
    )


def request_with_headers(url: str, method: str = "GET", headers: dict[str, str] | None = None) -> urllib.request.Request:
    merged = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if headers:
        merged.update(headers)
    return urllib.request.Request(url, method=method, headers=merged)


def probe_audio(url: str) -> dict[str, Any]:
    try:
        req = request_with_headers(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=30) as response:
            return {
                "status": response.status,
                "final_url": response.geturl(),
                "content_type": response.headers.get("Content-Type"),
                "content_length": int(response.headers["Content-Length"])
                if response.headers.get("Content-Length", "").isdigit()
                else None,
                "content_range": response.headers.get("Content-Range"),
                "probe_method": "HEAD",
            }
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError):
        req = request_with_headers(url, method="GET", headers={"Range": "bytes=0-0"})
        with urllib.request.urlopen(req, timeout=30) as response:
            return {
                "status": response.status,
                "final_url": response.geturl(),
                "content_type": response.headers.get("Content-Type"),
                "content_length": int(response.headers["Content-Length"])
                if response.headers.get("Content-Length", "").isdigit()
                else None,
                "content_range": response.headers.get("Content-Range"),
                "probe_method": "GET range",
            }


def extension_for_audio(audio_url: str, probe: dict[str, Any]) -> str:
    for candidate in (probe.get("final_url"), audio_url):
        if isinstance(candidate, str):
            suffix = Path(urllib.parse.urlparse(candidate).path).suffix.lower()
            if suffix in SUPPORTED_AUDIO_EXTENSIONS:
                return suffix
    content_type = str(probe.get("content_type") or "").split(";", 1)[0].strip().lower()
    if content_type in CONTENT_TYPE_EXTENSIONS:
        return CONTENT_TYPE_EXTENSIONS[content_type]
    guessed = mimetypes.guess_extension(content_type)
    return guessed or ".audio"


def safe_filename(value: str, fallback: str) -> str:
    cleaned = re.sub(r"[/:\\\0]+", "-", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = cleaned.strip(". ")
    return cleaned[:120] or fallback


def download_audio(url: str, destination: Path) -> dict[str, Any]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    req = request_with_headers(url)
    downloaded = 0
    with urllib.request.urlopen(req, timeout=60) as response, destination.open("wb") as out:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)
            downloaded += len(chunk)
        final_url = response.geturl()
        content_type = response.headers.get("Content-Type")
    return {
        "audio_path": str(destination),
        "downloaded_size": downloaded,
        "download_final_url": final_url,
        "download_content_type": content_type,
    }


def compact_episode(podcast: dict[str, Any], episode: dict[str, Any]) -> dict[str, Any]:
    artwork = episode.get("artworkUrl600") or podcast.get("artworkUrl600") or episode.get("artworkUrl100")
    episode_guid = episode.get("episodeGuid")
    publisher_page_url = episode_guid if isinstance(episode_guid, str) and episode_guid.startswith(("http://", "https://")) else None
    return {
        "podcast_title": episode.get("collectionName") or podcast.get("collectionName"),
        "podcast_author": episode.get("artistName") or podcast.get("artistName"),
        "episode_title": episode.get("trackName"),
        "episode_id": episode.get("trackId"),
        "podcast_id": episode.get("collectionId") or podcast.get("collectionId"),
        "release_date": episode.get("releaseDate"),
        "duration_millis": episode.get("trackTimeMillis"),
        "episode_guid": episode_guid,
        "feed_url": episode.get("feedUrl") or podcast.get("feedUrl"),
        "episode_url": episode.get("episodeUrl"),
        "apple_episode_url": episode.get("trackViewUrl"),
        "apple_collection_url": episode.get("collectionViewUrl") or podcast.get("collectionViewUrl"),
        "publisher_page_url": publisher_page_url,
        "short_description": episode.get("shortDescription"),
        "description": episode.get("description"),
        "artwork_url": artwork,
    }


def main() -> None:
    args = parse_args()
    parsed_url = parse_apple_url(args.url)
    podcast, episode, lookup_url = find_episode(parsed_url)
    compact = compact_episode(podcast, episode)
    audio_url = compact.get("episode_url")
    if not isinstance(audio_url, str) or not audio_url:
        raise SystemExit("Apple lookup matched the episode but did not provide an episodeUrl. Use browser capture fallback.")

    probe = probe_audio(audio_url)
    cache_root = Path(args.cache_root).expanduser().resolve()
    cache_dir = cache_root / f"{parsed_url['podcast_id']}-{parsed_url['episode_id']}"
    note_stem = safe_filename(
        f"{datetime.now().date().isoformat()}_{compact.get('podcast_title')}_{compact.get('episode_title')}",
        f"{parsed_url['podcast_id']}-{parsed_url['episode_id']}",
    )
    payload: dict[str, Any] = {
        "resolved_at": datetime.now(timezone.utc).isoformat(),
        "resolver": "apple_lookup",
        "lookup_url": lookup_url,
        "input": parsed_url,
        "episode": compact,
        "audio": {
            "audio_url": audio_url,
            **probe,
        },
        "cache_dir": str(cache_dir),
        "episode_json_path": str(cache_dir / "episode.json"),
        "suggested_note_stem": note_stem,
    }
    if args.download:
        extension = extension_for_audio(audio_url, probe)
        payload["audio"].update(download_audio(audio_url, cache_dir / f"audio{extension}"))

    cache_dir.mkdir(parents=True, exist_ok=True)
    (cache_dir / "episode.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Resolved: {compact.get('podcast_title')} - {compact.get('episode_title')}")
        print(f"Audio: {probe.get('final_url')}")
        print(f"Cache: {cache_dir}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
