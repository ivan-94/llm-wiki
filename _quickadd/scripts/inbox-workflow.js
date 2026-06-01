const INBOX_ROOT = "human/inbox";
const RAW_ROOT = "human/raw";
const ARCHIVE_ROOT = "human/archived";

const ACTIONS = [
  { id: "mark-read", label: "Mark read" },
  { id: "reset-unread", label: "Reset unread" },
  { id: "send-to-raw", label: "Send to raw" },
  { id: "archive", label: "Archive" },
];

module.exports = async (params) => {
  const ctx = createContext(params);
  const action = await selectAction(ctx);

  const file = await selectInboxFile(ctx);

  switch (action) {
    case "mark-read":
      await markRead(ctx, file);
      break;
    case "reset-unread":
      await resetUnread(ctx, file);
      break;
    case "send-to-raw":
      await moveToRaw(ctx, file);
      break;
    case "archive":
      await archive(ctx, file);
      break;
    default:
      throw new Error(`Unsupported inbox action: ${action}`);
  }
};

function createContext(params) {
  if (!params || !params.app) {
    throw new Error("QuickAdd did not provide an Obsidian app context.");
  }

  return {
    app: params.app,
    quickAddApi: params.quickAddApi,
    obsidian: params.obsidian,
    variables: params.variables || {},
  };
}

async function selectAction(ctx) {
  const requested = normalizeAction(
    getVariable(ctx, "action") ||
      getVariable(ctx, "value-action") ||
      getVariable(ctx, "inbox_action"),
  );

  if (requested) {
    return requested;
  }

  return suggester(
    ctx,
    "Choose inbox action",
    ACTIONS.map((action) => action.label),
    ACTIONS.map((action) => action.id),
  );
}

function normalizeAction(value) {
  if (!value) {
    return null;
  }

  const normalized = String(value).trim().toLowerCase();
  const aliases = {
    read: "mark-read",
    "mark-read": "mark-read",
    unread: "reset-unread",
    "reset-unread": "reset-unread",
    raw: "send-to-raw",
    "send-raw": "send-to-raw",
    "send-to-raw": "send-to-raw",
    archive: "archive",
    archived: "archive",
  };

  return aliases[normalized] || null;
}

async function selectInboxFile(ctx) {
  const requestedPath = getVariable(ctx, "path") || getVariable(ctx, "file");
  if (requestedPath) {
    const requestedFile = ctx.app.vault.getAbstractFileByPath(
      normalizePath(requestedPath),
    );
    if (isInboxNote(requestedFile)) {
      return requestedFile;
    }

    throw new Error(`Not an inbox markdown note: ${requestedPath}`);
  }

  const activeFile = ctx.app.workspace.getActiveFile();
  if (isInboxNote(activeFile)) {
    return activeFile;
  }

  const candidates = ctx.app.vault
    .getMarkdownFiles()
    .filter(isInboxNote)
    .sort((left, right) => left.path.localeCompare(right.path));

  if (candidates.length === 0) {
    throw new Error("No inbox markdown notes found.");
  }

  return suggester(
    ctx,
    "Choose inbox note",
    candidates.map((file) => file.path),
    candidates,
  );
}

function isInboxNote(file) {
  return Boolean(
    file &&
      file.path &&
      file.extension === "md" &&
      file.path.startsWith(`${INBOX_ROOT}/`) &&
      !file.path.includes("/assets/"),
  );
}

async function markRead(ctx, file) {
  await updateFrontMatter(ctx, file, (frontmatter) => {
    frontmatter.inbox_status = "read";
    frontmatter.inbox_read_at = frontmatter.inbox_read_at || localDate();
  });

  notice(ctx, `Marked read: ${file.path}`);
}

async function resetUnread(ctx, file) {
  await updateFrontMatter(ctx, file, (frontmatter) => {
    frontmatter.inbox_status = "unread";
    delete frontmatter.inbox_read_at;
  });

  notice(ctx, `Reset unread: ${file.path}`);
}

async function moveToRaw(ctx, file) {
  const oldPath = file.path;
  const targetPath = promotedPath(oldPath, RAW_ROOT);
  const confirmed = await confirm(
    ctx,
    "Send to raw",
    `Move ${oldPath} to ${targetPath}?`,
  );

  if (!confirmed) {
    notice(ctx, "Send to raw cancelled.");
    return;
  }

  const movedFile = await moveNoteWithAssets(ctx, file, RAW_ROOT);

  await updateFrontMatter(ctx, movedFile, (frontmatter) => {
    const previousStatus = frontmatter.inbox_status || "unknown";
    frontmatter.inbox_status = "raw";
    frontmatter.previous_inbox_status = previousStatus;
    frontmatter.raw_path = targetPath;
    frontmatter.promoted_from = oldPath;
    frontmatter.promoted_at = localDate();
    frontmatter.source_type = "promoted-inbox";
    frontmatter.ingest_policy = "allowed";
    delete frontmatter.archive_reason;
  });
  await rewriteAssetLinks(ctx, movedFile, RAW_ROOT);

  await openPath(ctx, targetPath);
  notice(ctx, `Moved to raw: ${targetPath}`);
}

async function archive(ctx, file) {
  const oldPath = file.path;
  const targetPath = promotedPath(oldPath, ARCHIVE_ROOT);
  const reason =
    (await input(ctx, "Archive reason", "optional")) || "not specified";
  const confirmed = await confirm(
    ctx,
    "Archive inbox note",
    `Move ${oldPath} to ${targetPath}?`,
  );

  if (!confirmed) {
    notice(ctx, "Archive cancelled.");
    return;
  }

  const movedFile = await moveNoteWithAssets(ctx, file, ARCHIVE_ROOT);

  await updateFrontMatter(ctx, movedFile, (frontmatter) => {
    const previousStatus = frontmatter.inbox_status || "unknown";
    frontmatter.inbox_status = "archived";
    frontmatter.previous_inbox_status = previousStatus;
    frontmatter.archived_from = oldPath;
    frontmatter.archived_at = localDate();
    frontmatter.archive_reason = reason;
  });
  await rewriteAssetLinks(ctx, movedFile, ARCHIVE_ROOT);

  await openPath(ctx, targetPath);
  notice(ctx, `Archived: ${targetPath}`);
}

async function moveNoteWithAssets(ctx, file, targetRoot) {
  const oldPath = file.path;
  const targetPath = promotedPath(oldPath, targetRoot);
  const content = await ctx.app.vault.read(file);
  const assetMoves = await collectAssetMoves(
    ctx,
    oldPath,
    content,
    targetRoot,
  );

  await assertMissing(ctx, targetPath, "target note");
  for (const move of assetMoves) {
    await assertMissing(ctx, move.to, "target asset directory");
  }

  await ensureFolder(ctx, dirname(targetPath));
  for (const move of assetMoves) {
    await ensureFolder(ctx, dirname(move.to));
  }

  await renameAbstractFile(ctx, file, targetPath);

  for (const move of assetMoves) {
    const assetFolder = ctx.app.vault.getAbstractFileByPath(move.from);
    if (!assetFolder) {
      throw new Error(`Asset directory disappeared before move: ${move.from}`);
    }

    await renameAbstractFile(ctx, assetFolder, move.to);
  }

  const movedFile = ctx.app.vault.getAbstractFileByPath(targetPath);
  if (!movedFile) {
    throw new Error(`Move finished, but target note was not found: ${targetPath}`);
  }

  return movedFile;
}

async function collectAssetMoves(ctx, oldPath, content, targetRoot) {
  const assetDirs = new Set([
    `${dirname(oldPath)}/assets/${stem(basename(oldPath))}`,
  ]);

  for (const assetPath of extractInboxAssetPaths(content)) {
    assetDirs.add(assetPath);
  }

  const moves = [];
  for (const assetDir of assetDirs) {
    if (await exists(ctx, assetDir)) {
      moves.push({
        from: assetDir,
        to: replaceInboxRoot(assetDir, targetRoot),
      });
    }
  }

  return moves;
}

function extractInboxAssetPaths(content) {
  const paths = new Set();
  const regex = /human\/inbox\/[^\]\)\n]*?\/assets\/[^\/\]\)\n]+/g;
  let match;

  while ((match = regex.exec(content)) !== null) {
    paths.add(match[0]);
  }

  return paths;
}

async function rewriteAssetLinks(ctx, file, targetRoot) {
  const content = await ctx.app.vault.read(file);
  const rewritten = content
    .replace(
      /!\[\[(human\/inbox\/[^\]\|#]+)((?:[|#][^\]]*)?)\]\]/g,
      (full, path, suffix) => {
        if (!path.includes("/assets/")) {
          return full;
        }

        return `![[${replaceInboxRoot(path, targetRoot)}${suffix}]]`;
      },
    )
    .replace(/(!\[[^\]]*\]\()([^)]+)(\))/g, (full, prefix, path, suffix) => {
      const cleanPath = path.trim();
      if (
        !cleanPath.startsWith(`${INBOX_ROOT}/`) ||
        !cleanPath.includes("/assets/")
      ) {
        return full;
      }

      return `${prefix}${replaceInboxRoot(cleanPath, targetRoot)}${suffix}`;
    });

  if (rewritten !== content) {
    await ctx.app.vault.modify(file, rewritten);
  }
}

async function updateFrontMatter(ctx, file, mutator) {
  if (!ctx.app.fileManager || !ctx.app.fileManager.processFrontMatter) {
    throw new Error("Obsidian fileManager.processFrontMatter is unavailable.");
  }

  await ctx.app.fileManager.processFrontMatter(file, mutator);
}

async function renameAbstractFile(ctx, file, targetPath) {
  if (ctx.app.fileManager && ctx.app.fileManager.renameFile) {
    await ctx.app.fileManager.renameFile(file, targetPath);
    return;
  }

  if (file.extension) {
    await ctx.app.vault.rename(file, targetPath);
    return;
  }

  await ctx.app.vault.adapter.rename(file.path, targetPath);
}

function promotedPath(path, targetRoot) {
  if (!path.startsWith(`${INBOX_ROOT}/`)) {
    throw new Error(`Path is not under ${INBOX_ROOT}: ${path}`);
  }

  return `${targetRoot}/inbox/${path.slice(INBOX_ROOT.length + 1)}`;
}

function replaceInboxRoot(path, targetRoot) {
  return path.replace(
    new RegExp(`^${escapeRegExp(INBOX_ROOT)}/`),
    `${targetRoot}/inbox/`,
  );
}

async function assertMissing(ctx, path, label) {
  if (await exists(ctx, path)) {
    throw new Error(`${label} already exists, refusing to overwrite: ${path}`);
  }
}

async function exists(ctx, path) {
  return ctx.app.vault.adapter.exists(normalizePath(path));
}

async function ensureFolder(ctx, folderPath) {
  const folder = normalizePath(folderPath);
  if (!folder || folder === ".") {
    return;
  }

  const segments = folder.split("/");
  let current = "";

  for (const segment of segments) {
    current = current ? `${current}/${segment}` : segment;
    if (!(await exists(ctx, current))) {
      await ctx.app.vault.createFolder(current);
    }
  }
}

async function openPath(ctx, path) {
  const file = ctx.app.vault.getAbstractFileByPath(path);
  if (!file) {
    throw new Error(`Cannot open missing file: ${path}`);
  }

  await ctx.app.workspace.getLeaf(true).openFile(file);
}

async function suggester(ctx, title, labels, values) {
  if (!ctx.quickAddApi || !ctx.quickAddApi.suggester) {
    throw new Error(`${title}: QuickAdd suggester is unavailable.`);
  }

  const selected = await ctx.quickAddApi.suggester(labels, values);
  if (!selected) {
    throw new Error(`${title} cancelled.`);
  }

  return selected;
}

async function confirm(ctx, title, message) {
  if (ctx.quickAddApi && ctx.quickAddApi.yesNoPrompt) {
    return ctx.quickAddApi.yesNoPrompt(title, message);
  }

  if (typeof window !== "undefined" && window.confirm) {
    return window.confirm(`${title}\n\n${message}`);
  }

  return false;
}

async function input(ctx, title, placeholder) {
  if (ctx.quickAddApi && ctx.quickAddApi.inputPrompt) {
    return ctx.quickAddApi.inputPrompt(title, placeholder);
  }

  if (typeof window !== "undefined" && window.prompt) {
    return window.prompt(title, "");
  }

  return "";
}

function notice(ctx, message) {
  if (ctx.obsidian && ctx.obsidian.Notice) {
    new ctx.obsidian.Notice(message);
    return;
  }

  console.log(message);
}

function getVariable(ctx, key) {
  if (!ctx.variables) {
    return undefined;
  }

  if (typeof ctx.variables.get === "function") {
    const value = ctx.variables.get(key);
    if (value !== undefined) {
      return value;
    }
  }

  return ctx.variables[key];
}

function normalizePath(path) {
  return String(path).replace(/^\/+/, "").replace(/\/+/g, "/");
}

function dirname(path) {
  const index = path.lastIndexOf("/");
  return index === -1 ? "" : path.slice(0, index);
}

function basename(path) {
  const index = path.lastIndexOf("/");
  return index === -1 ? path : path.slice(index + 1);
}

function stem(filename) {
  return filename.replace(/\.md$/i, "");
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function localDate() {
  const date = new Date();
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");

  return `${year}-${month}-${day}`;
}
