#!/usr/bin/env bash
# Idempotent Cloud Agent bootstrap for PediRes_AI_1.
# Installs slides/workshops/requirements.txt when present, then a root
# requirements.txt / pyproject.toml / package.json if those appear.
set -euo pipefail

echo "=== PediRes_AI_1 install ==="
python3 --version
node --version
git --version

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -f slides/workshops/requirements.txt ]]; then
  python3 -m pip install --user -r slides/workshops/requirements.txt
fi

if [[ -f requirements.txt ]]; then
  python3 -m pip install --user -r requirements.txt
fi

if [[ -f pyproject.toml ]]; then
  python3 -m pip install --user -e .
fi

if [[ -f package-lock.json ]]; then
  npm ci
elif [[ -f package.json ]]; then
  npm install
fi

echo "=== PediRes_AI_1 install complete ==="
