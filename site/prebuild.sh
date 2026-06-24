#!/bin/bash
# Copy markdown files from repo into VitePress src directory
# Runs before vitepress build so CI doesn't depend on symlinks

set -e
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$(dirname "$0")/src"

mkdir -p "$SRC/exercises" "$SRC/programs" "$SRC/core" "$SRC/crosscutting" "$SRC/system_guides"

cp "$REPO_ROOT"/exercises/*.md "$SRC/exercises/"
cp "$REPO_ROOT"/programs/**/*.md "$SRC/programs/" 2>/dev/null || \
  find "$REPO_ROOT/programs" -name "*.md" -exec cp {} "$SRC/programs/" \;
cp "$REPO_ROOT"/core/*.md "$SRC/core/"
cp "$REPO_ROOT"/system_guides/*.md "$SRC/system_guides/"

# Flatten crosscutting subdirectories
find "$REPO_ROOT/crosscutting" -name "*.md" -exec cp {} "$SRC/crosscutting/" \;

# Copy llms.txt as a site page (for search engine indexing)
cp "$REPO_ROOT/llms.txt" "$SRC/llms-full.md"

echo "Copied files to site/src/"
ls "$SRC/exercises/" | wc -l | xargs -I{} echo "  exercises: {}"
ls "$SRC/programs/" | wc -l | xargs -I{} echo "  programs: {}"
ls "$SRC/core/" | wc -l | xargs -I{} echo "  core: {}"
ls "$SRC/crosscutting/" | wc -l | xargs -I{} echo "  crosscutting: {}"
