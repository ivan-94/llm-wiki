const { Notice, Plugin } = require("obsidian");

const APPLY_DELAY_MS = 120;

const COLOR_GROUPS = [
  {
    query: "path:human  ",
    color: {
      a: 1,
      rgb: 14048348,
    },
  },
  {
    query: "path:sources  ",
    color: {
      a: 1,
      rgb: 9013641,
    },
  },
  {
    query: "path:concepts  ",
    color: {
      a: 1,
      rgb: 6058198,
    },
  },
  {
    query: "path:entities  ",
    color: {
      a: 1,
      rgb: 11392604,
    },
  },
  {
    query: "path:synthesis  ",
    color: {
      a: 1,
      rgb: 6084188,
    },
  },
];

const LOCAL_GRAPH_DEFAULTS = {
  "collapse-filter": false,
  search: "-file:index.md -path:maps  ",
  localJumps: 2,
  localBacklinks: true,
  localForelinks: true,
  localInterlinks: false,
  showTags: false,
  showAttachments: false,
  hideUnresolved: false,
  "collapse-color-groups": false,
  colorGroups: COLOR_GROUPS,
  "collapse-display": false,
  showArrow: true,
  textFadeMultiplier: -1.4,
  nodeSizeMultiplier: 2.13443576388889,
  lineSizeMultiplier: 1.10381944444444,
  "collapse-forces": false,
  centerStrength: 0.233984375,
  repelStrength: 12.0633680555556,
  linkStrength: 0.827039930555556,
  linkDistance: 326,
  scale: 1,
  close: false,
};

module.exports = class AiWikiLocalGraphDefaultsPlugin extends Plugin {
  async onload() {
    this.applyTimer = null;
    this.appliedLeaves = new WeakSet();

    this.addCommand({
      id: "apply-local-graph-defaults",
      name: "AI Wiki: Apply local graph defaults",
      callback: async () => {
        const count = await this.applyDefaultsToAll({ force: true });
        new Notice(`Applied local graph defaults to ${count} pane${count === 1 ? "" : "s"}.`);
      },
    });

    this.registerEvent(
      this.app.workspace.on("layout-change", () => this.scheduleApply()),
    );
    this.registerEvent(
      this.app.workspace.on("active-leaf-change", () => this.scheduleApply()),
    );

    this.app.workspace.onLayoutReady(() => this.scheduleApply());
  }

  onunload() {
    if (this.applyTimer) {
      window.clearTimeout(this.applyTimer);
    }
  }

  scheduleApply() {
    if (this.applyTimer) {
      window.clearTimeout(this.applyTimer);
    }
    this.applyTimer = window.setTimeout(() => {
      this.applyDefaultsToAll({ force: false });
    }, APPLY_DELAY_MS);
  }

  async applyDefaultsToAll({ force }) {
    const leaves = this.getLeaves();
    let count = 0;

    for (const leaf of leaves) {
      if (!this.isLocalGraphLeaf(leaf)) {
        continue;
      }
      if (!force && this.appliedLeaves.has(leaf)) {
        continue;
      }

      try {
        const applied = await this.applyDefaultsToLeaf(leaf);
        if (applied) {
          this.appliedLeaves.add(leaf);
          count += 1;
        }
      } catch (error) {
        console.error("Failed to apply AI Wiki local graph defaults", error);
      }
    }

    return count;
  }

  getLeaves() {
    const leaves = new Set();
    if (typeof this.app.workspace.getLeavesOfType === "function") {
      for (const leaf of this.app.workspace.getLeavesOfType("localgraph")) {
        leaves.add(leaf);
      }
    }
    if (typeof this.app.workspace.iterateAllLeaves === "function") {
      this.app.workspace.iterateAllLeaves((leaf) => leaves.add(leaf));
    }
    return Array.from(leaves);
  }

  isLocalGraphLeaf(leaf) {
    const viewState = this.getViewState(leaf);
    if (viewState && viewState.type === "localgraph") {
      return true;
    }
    return leaf.view && typeof leaf.view.getViewType === "function" && leaf.view.getViewType() === "localgraph";
  }

  getViewState(leaf) {
    if (!leaf || typeof leaf.getViewState !== "function") {
      return null;
    }
    return leaf.getViewState();
  }

  async applyDefaultsToLeaf(leaf) {
    const viewState = this.getViewState(leaf);
    if (!viewState || viewState.type !== "localgraph") {
      return false;
    }

    const state = viewState.state || {};
    const currentOptions = state.options || {};
    const nextOptions = {
      ...currentOptions,
      ...LOCAL_GRAPH_DEFAULTS,
      colorGroups: cloneColorGroups(),
    };

    if (sameJson(currentOptions, nextOptions)) {
      return true;
    }

    await leaf.setViewState(
      {
        ...viewState,
        state: {
          ...state,
          options: nextOptions,
        },
      },
      { focus: false },
    );

    return true;
  }
};

function cloneColorGroups() {
  return COLOR_GROUPS.map((group) => ({
    query: group.query,
    color: {
      ...group.color,
    },
  }));
}

function sameJson(left, right) {
  return JSON.stringify(left) === JSON.stringify(right);
}
