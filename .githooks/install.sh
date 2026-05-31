#!/bin/sh
set -eu

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

if [ ! -f ".githooks/post-commit" ]; then
  echo "install-git-hooks: missing .githooks/post-commit" >&2
  exit 1
fi

chmod +x .githooks/post-commit
git config core.hooksPath .githooks

echo "install-git-hooks: core.hooksPath=$(git config --get core.hooksPath)"
