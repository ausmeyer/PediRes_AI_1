#!/usr/bin/env bash
# Render the lecture into docs/ for GitHub Pages.
# Default is linked assets (fast to render and to open).
# Pass --self-contained for a single-file USB freeze when there is no Wi-Fi.
set -euo pipefail
cd "$(dirname "$0")"

if [[ "${1:-}" == "--self-contained" ]]; then
  quarto render lecture.qmd -M embed-resources:true
else
  quarto render lecture.qmd
fi

# Quarto can retain older linked figures in _site. Mirror the authored set so a
# rerender publishes the current artwork and removes obsolete generated files.
rsync -a --delete assets/figures/ _site/assets/figures/

# Drop stale single-file builds so they are not copied into docs/.
rm -f _site/lecture.html

mkdir -p ../docs
if command -v rsync >/dev/null 2>&1; then
  rsync -a --delete --exclude .nojekyll _site/ ../docs/
else
  # Fallback when rsync is missing: replace docs contents except .nojekyll.
  find ../docs -mindepth 1 -maxdepth 1 ! -name .nojekyll -exec rm -rf {} +
  cp -a _site/. ../docs/
fi
touch ../docs/.nojekyll
echo "Wrote $(cd .. && pwd)/docs/index.html ($(wc -c < ../docs/index.html) bytes)"
