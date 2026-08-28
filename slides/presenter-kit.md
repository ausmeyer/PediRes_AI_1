# Presenter kit — six simple demonstrations

These are presenter-run demonstrations using synthetic teaching material. The detailed source notes are in [`../briefing/workshops.md`](../briefing/workshops.md).

## Before the lecture

1. From the repository root, prepare the demonstration folders:

   ```bash
   ./slides/workshops/prepare_demo_folders.sh /tmp/peds-ai-live-demos
   ```

2. Open the lecture, Codex, and `/tmp/peds-ai-live-demos/`.
3. Pull and test the local model while online: `ollama pull qwen3.8`.
4. Open the AAP guideline and correction links supplied in Demonstration 4.
5. Close the EHR, email, messages, and anything showing a real patient name.

For each demonstration: explain the practical job, run the supplied prompt, open the result, and verify one detail aloud.

## 1 — Make office files with Codex

**Folder:** `/tmp/peds-ai-live-demos/01-office-files/`

1. Open the folder in Codex and paste `PROMPT.md`.
2. Open the three generated files.
3. Show that the letter ends with `This is a teaching example.`
4. Show six spreadsheet rows with no medication column and citation placeholders in the slide deck.

**Takeaway:** Codex can make useful files, but the presenter still opens and checks them.

## 2 — Build a journal-club page from one PDF

**Folder:** `/tmp/peds-ai-live-demos/02-journal-club/`

1. Start a fresh Codex task with web access off and paste `PROMPT.md`.
2. Open the generated `docs/index.html` and `SOURCE_LEDGER.md`.
3. Find the claim that the review included 11 studies.
4. Open the supplied PDF to viewer page 3 and confirm that number in the abstract.

**Takeaway:** Move from a named source to an artifact, then back to the source for verification.

## 3 — Run a local model offline

**Folder:** `/tmp/peds-ai-live-demos/03-offline-ollama/`

1. Turn Wi-Fi off.
2. Run:

   ```bash
   cd /tmp/peds-ai-live-demos/03-offline-ollama
   ollama run qwen3.8 < demo3_ollama_prompt.txt
   ```

3. Show that the missing current weight and numeric urine output remain `MISSING`.
4. Turn Wi-Fi back on before the next demonstration.

**Takeaway:** Local execution controls where the prompt goes; it does not guarantee accuracy.

## 4 — Compare three source conditions

**Parent folder:** `/tmp/peds-ai-live-demos/04-source-conditions/`

1. Start a fresh Codex task in `A-no-source/`, keep web access off, and paste `PROMPT.md`.
2. Start a fresh task in `B-guideline/`, turn web access on, and paste `PROMPT.md`.
3. Start a fresh task in `C-guideline-and-correction/` and paste `PROMPT.md`.
4. Compare whether each answer names its source, uses the correct age group, asks for the missing urinalysis and inflammatory markers, and reviews the correction.

**Takeaway:** The allowed source material changes how traceable and complete an answer can be.

## 5 — Repair and test an existing page

**Folder:** `/tmp/peds-ai-live-demos/05-repair-page/`

1. Open `broken_attendance.html`, enter `4`, and show that nothing highlights.
2. Open the folder in Codex and paste `PROMPT.md`.
3. Reload the page and enter `4`; only Week 4 should turn orange and report `25`.
4. Enter `9`; no bar should highlight and the page should ask for a week from 1 to 8.

**Takeaway:** Codex can inspect, edit, and test the artifact itself.

## 6 — Build a brief from a fixed source packet

**Folder:** `/tmp/peds-ai-live-demos/06-source-packet/`

1. Start a fresh Codex task with web access off and paste `PROMPT.md`.
2. Open the generated `evidence_brief.md`.
3. Confirm that it distinguishes the Artsi systematic review from the WHO and FDA discussion papers.
4. Verify the FDA document type on PDF viewer page 2, then show that the off-packet question begins `NOT IN PACKET`.

**Takeaway:** A fixed packet makes synthesis easier to inspect and keeps absent evidence visibly absent.

## Close

Return to the lecture and finish with **Six habits to remember**, **Three questions before you copy**, and Q&A.
