const { MarkdownView, Menu, Notice, Plugin } = require("obsidian");

const INBOX_ROOT = "human/inbox/";
const RAW_INBOX_ROOT = "human/raw/inbox/";
const ARCHIVED_INBOX_ROOT = "human/archived/inbox/";
const BOARD_PATH = "human/inbox/inbox.base";
const QUICKADD_CHOICE = "Inbox: Action";

module.exports = class AiWikiInboxToolbarPlugin extends Plugin {
  async onload() {
    this.renderTimer = null;
    this.actionEls = [];

    this.registerEvent(
      this.app.workspace.on("active-leaf-change", () => this.scheduleRender()),
    );
    this.registerEvent(
      this.app.workspace.on("file-open", () => this.scheduleRender()),
    );
    this.registerEvent(
      this.app.workspace.on("layout-change", () => this.scheduleRender()),
    );
    this.registerEvent(
      this.app.metadataCache.on("changed", (file) => {
        const active = this.app.workspace.getActiveFile();
        if (active && file && active.path === file.path) {
          this.scheduleRender();
        }
      }),
    );

    this.addCommand({
      id: "refresh-inbox-toolbar",
      name: "Refresh inbox action",
      callback: () => this.render(),
    });

    this.scheduleRender();
  }

  onunload() {
    if (this.renderTimer) {
      window.clearTimeout(this.renderTimer);
    }
    this.removeActions();
  }

  scheduleRender() {
    if (this.renderTimer) {
      window.clearTimeout(this.renderTimer);
    }
    this.renderTimer = window.setTimeout(() => this.render(), 80);
  }

  render() {
    this.removeActions();

    const view = this.app.workspace.getActiveViewOfType(MarkdownView);
    if (!view || !view.file || !this.shouldShowForFile(view.file)) {
      return;
    }

    let actionEl = null;
    actionEl = view.addAction("inbox", this.actionTitle(view.file), (event) => {
      this.showMenu(event, view.file, actionEl);
    });

    actionEl.classList.add("ai-wiki-inbox-title-action");
    this.actionEls.push(actionEl);
  }

  removeActions() {
    for (const actionEl of this.actionEls) {
      actionEl.remove();
    }
    this.actionEls = [];

    document
      .querySelectorAll(".ai-wiki-inbox-toolbar")
      .forEach((toolbar) => toolbar.remove());
  }

  shouldShowForFile(file) {
    if (!file || file.extension !== "md") {
      return false;
    }
    if (file.path.includes("/assets/")) {
      return false;
    }

    return (
      file.path.startsWith(INBOX_ROOT) ||
      file.path.startsWith(RAW_INBOX_ROOT) ||
      file.path.startsWith(ARCHIVED_INBOX_ROOT)
    );
  }

  actionTitle(file) {
    const status = this.getInboxStatus(file) || this.statusFromPath(file.path);
    return `Inbox workflow: ${status}`;
  }

  getInboxStatus(file) {
    const cache = this.app.metadataCache.getFileCache(file);
    return cache && cache.frontmatter && cache.frontmatter.inbox_status;
  }

  statusFromPath(path) {
    if (path.startsWith(RAW_INBOX_ROOT)) {
      return "raw";
    }
    if (path.startsWith(ARCHIVED_INBOX_ROOT)) {
      return "archived";
    }
    return "inbox";
  }

  showMenu(event, file, actionEl) {
    const menu = new Menu();
    const status = this.getInboxStatus(file) || this.statusFromPath(file.path);

    menu.addItem((item) => {
      item
        .setTitle(`Status: ${status}`)
        .setIcon("info")
        .setDisabled(true);
    });

    if (file.path.startsWith(INBOX_ROOT)) {
      menu.addSeparator();
      this.addQuickAddItem(menu, "Mark read", "check-circle", "mark-read", file);
      this.addQuickAddItem(menu, "Reset unread", "rotate-ccw", "reset-unread", file);
      this.addQuickAddItem(menu, "Send to raw", "folder-input", "send-to-raw", file);
      this.addQuickAddItem(menu, "Archive", "archive", "archive", file);
    }

    menu.addSeparator();
    this.addOpenItem(menu, "Open inbox board", "table", BOARD_PATH);

    if (event && event instanceof MouseEvent) {
      menu.showAtMouseEvent(event);
      return;
    }

    const rect = actionEl.getBoundingClientRect();
    menu.showAtPosition({ x: rect.left, y: rect.bottom });
  }

  addQuickAddItem(menu, title, icon, action, file) {
    menu.addItem((item) => {
      item.setTitle(title).setIcon(icon).onClick(() => {
        this.openQuickAdd(action, file);
      });
    });
  }

  addOpenItem(menu, title, icon, path) {
    menu.addItem((item) => {
      item.setTitle(title).setIcon(icon).onClick(async () => {
        const file = this.app.vault.getAbstractFileByPath(path);
        if (!file) {
          new Notice(`Missing file: ${path}`);
          return;
        }
        await this.app.workspace.getLeaf(true).openFile(file);
      });
    });
  }

  openQuickAdd(action, file) {
    const params = [
      ["choice", QUICKADD_CHOICE],
      ["value-action", action],
      ["value-path", file.path],
    ]
      .map(([key, value]) => `${key}=${encodeURIComponent(value)}`)
      .join("&");

    window.location.href = `obsidian://quickadd?${params}`;
  }
};
