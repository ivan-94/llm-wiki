const { MarkdownView, Menu, Notice, Plugin } = require("obsidian");

const INBOX_ROOT = "human/inbox/";
const RAW_INBOX_ROOT = "human/raw/inbox/";
const ARCHIVED_INBOX_ROOT = "human/archived/inbox/";
const BOARD_PATH = "human/inbox/inbox.base";
const QUICKADD_CHOICE = "Inbox: Action";
const LOCAL_GRAPH_COMMAND_IDS = ["graph:open-local", "graph:open-local-graph"];
const TOGGLE_PROPERTIES_COMMAND = "editor:toggle-fold-properties";

module.exports = class AiWikiInboxToolbarPlugin extends Plugin {
  async onload() {
    this.renderTimer = null;
    this.collapseTimers = [];
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
    this.clearCollapseTimers();
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
    if (!view || !view.file || view.file.extension !== "md") {
      return;
    }

    this.addLocalGraphAction(view);

    if (!this.shouldShowForFile(view.file)) {
      return;
    }

    let actionEl = null;
    actionEl = view.addAction("inbox", this.actionTitle(view.file), (event) => {
      this.showMenu(event, view.file, actionEl);
    });

    actionEl.classList.add("ai-wiki-inbox-title-action");
    this.actionEls.push(actionEl);
    this.scheduleCollapseProperties(view);
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

  addLocalGraphAction(view) {
    const actionEl = view.addAction("git-fork", "Open local graph", () => {
      this.openLocalGraph();
    });
    actionEl.classList.add("ai-wiki-local-graph-title-action");
    this.actionEls.push(actionEl);
  }

  openLocalGraph() {
    const commandId = this.findLocalGraphCommandId();
    if (!commandId) {
      new Notice("Could not find Obsidian local graph command.");
      return;
    }

    this.app.commands.executeCommandById(commandId);
  }

  findLocalGraphCommandId() {
    const commands = this.app.commands && this.app.commands.commands;
    if (!commands) {
      return null;
    }

    for (const commandId of LOCAL_GRAPH_COMMAND_IDS) {
      if (commands[commandId]) {
        return commandId;
      }
    }

    const matched = Object.entries(commands).find(([commandId, command]) => {
      const haystack = `${commandId} ${command.name || ""}`;
      return (
        commandId.startsWith("graph:") &&
        /local graph|局部关系图谱|局部图谱/i.test(haystack)
      );
    });

    return matched ? matched[0] : null;
  }

  scheduleCollapseProperties(view) {
    this.clearCollapseTimers();
    for (const delay of [80, 250, 700]) {
      const timer = window.setTimeout(() => {
        this.collapsePropertiesIfExpanded(view);
      }, delay);
      this.collapseTimers.push(timer);
    }
  }

  clearCollapseTimers() {
    for (const timer of this.collapseTimers || []) {
      window.clearTimeout(timer);
    }
    this.collapseTimers = [];
  }

  collapsePropertiesIfExpanded(view) {
    if (!view || !view.file || !this.shouldShowForFile(view.file)) {
      return;
    }
    if (!this.hasTogglePropertiesCommand()) {
      return;
    }

    const container = view.contentEl.querySelector(
      ".metadata-container, .frontmatter-container",
    );
    if (!container || this.isPropertiesCollapsed(container)) {
      return;
    }

    this.app.commands.executeCommandById(TOGGLE_PROPERTIES_COMMAND);
  }

  hasTogglePropertiesCommand() {
    return Boolean(
      this.app.commands &&
        this.app.commands.commands &&
        this.app.commands.commands[TOGGLE_PROPERTIES_COMMAND],
    );
  }

  isPropertiesCollapsed(container) {
    if (container.classList.contains("is-collapsed")) {
      return true;
    }

    const heading = container.querySelector(".metadata-properties-heading");
    if (heading && heading.classList.contains("is-collapsed")) {
      return true;
    }

    const content = container.querySelector(
      ".metadata-content, .metadata-properties",
    );
    if (!content) {
      return false;
    }

    const style = window.getComputedStyle(content);
    return (
      style.display === "none" ||
      style.visibility === "hidden" ||
      content.getBoundingClientRect().height === 0
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
