#!/usr/bin/env bash
# Render the lecture to ../docs/index.html (GitHub Pages /docs).
set -euo pipefail
cd "$(dirname "$0")"
quarto render lecture.qmd
# Quarto may clean the output dir; keep Jekyll from rewriting the deck.
touch ../docs/.nojekyll
# Figures are already inlined in index.html; don't publish a second copy.
rm -rf ../docs/assets
echo "Wrote $(cd .. && pwd)/docs/index.html"
