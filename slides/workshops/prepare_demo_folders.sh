#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/../.." && pwd)"
destination="${1:-/tmp/peds-ai-live-demos}"

if [[ -e "$destination" ]]; then
  echo "Refusing to overwrite existing destination: $destination" >&2
  echo "Choose a new empty path for this rehearsal." >&2
  exit 1
fi

mkdir -p \
  "$destination/01-office-files" \
  "$destination/02-journal-club/sources" \
  "$destination/03-offline-ollama" \
  "$destination/04-source-conditions/A-no-source" \
  "$destination/04-source-conditions/B-guideline" \
  "$destination/04-source-conditions/C-guideline-and-correction" \
  "$destination/05-repair-page" \
  "$destination/06-source-packet/sources"

cp "$script_dir/STEM.txt" "$destination/01-office-files/STEM.txt"
cp "$script_dir/demo1_prompt.txt" "$destination/01-office-files/PROMPT.txt"

cp "$repo_root/briefing/papers/s41746-026-03077-4_reference.pdf" \
  "$destination/02-journal-club/sources/OpenEvidence_systematic_review_2026.pdf"
cp "$script_dir/demo2_prompt.txt" "$destination/02-journal-club/PROMPT.txt"

cp "$script_dir/demo3_ollama_prompt.txt" "$destination/03-offline-ollama/"

cp "$script_dir/demo4_case.txt" "$destination/04-source-conditions/A-no-source/CASE.txt"
cp "$script_dir/demo4_prompt_a.txt" "$destination/04-source-conditions/A-no-source/PROMPT.txt"
cp "$script_dir/demo4_case.txt" "$destination/04-source-conditions/B-guideline/CASE.txt"
cp "$script_dir/demo4_sources_guideline.md" "$destination/04-source-conditions/B-guideline/SOURCES.md"
cp "$script_dir/demo4_prompt_b.txt" "$destination/04-source-conditions/B-guideline/PROMPT.txt"
cp "$script_dir/demo4_case.txt" "$destination/04-source-conditions/C-guideline-and-correction/CASE.txt"
cp "$script_dir/demo4_sources_with_correction.md" "$destination/04-source-conditions/C-guideline-and-correction/SOURCES.md"
cp "$script_dir/demo4_prompt_c.txt" "$destination/04-source-conditions/C-guideline-and-correction/PROMPT.txt"

cp "$script_dir/broken_attendance.html" "$destination/05-repair-page/"
cp "$script_dir/demo5_prompt.txt" "$destination/05-repair-page/PROMPT.txt"

cp "$script_dir/demo6_prompt.txt" "$destination/06-source-packet/PROMPT.txt"
cp "$script_dir/SOURCE_PACKET.md" "$destination/06-source-packet/"
cp "$repo_root/briefing/papers/B09667-eng.pdf" \
  "$destination/06-source-packet/sources/WHO_AI_evidence_policy_2026.pdf"
cp "$repo_root/briefing/papers/FDA-2026-N-7874-0001_attachment_1.pdf" \
  "$destination/06-source-packet/sources/FDA_GenAI_medical_devices_discussion_2026.pdf"
cp "$repo_root/briefing/papers/s41746-026-03077-4_reference.pdf" \
  "$destination/06-source-packet/sources/OpenEvidence_systematic_review_2026.pdf"

echo "Prepared six demonstration folders at: $destination"
