# Presenter kit — six live demonstrations

The canonical instructions are in [`../briefing/workshops.md`](../briefing/workshops.md). The lecture follows Demonstrations 1–6 in that order, then **six habits → three questions → The End / Q&A**. Backup slides begin after the closing slide.

## Prepare once

From the repository root:

```bash
./slides/workshops/prepare_demo_folders.sh /tmp/peds-ai-live-demos
```

The command creates a clean folder for each demonstration and copies every exact input into place. It refuses to overwrite an existing directory.

Before the room opens:

- Launch the lecture from `docs/index.html` and confirm speaker view.
- Open Codex on `/tmp/peds-ai-live-demos`.
- Confirm `python-docx`, `openpyxl`, and `python-pptx` for the Demonstration 1 fallback.
- Run `ollama pull qwen3.8`, test one response, then leave the model loaded.
- Open the official AAP guideline DOI `10.1542/peds.2021-052228` and correction DOI `10.1542/peds.2021-054063` in browser tabs.
- Keep `SYNTHETIC TEACHING CASE — NOT A REAL PATIENT` visible whenever a clinical stem is projected.
- Close the EHR, email, messaging, and any tab that could expose a real name.

## The delivery rhythm

For every demonstration:

1. Predict one likely failure.
2. Paste the supplied `PROMPT.md` or run the supplied Ollama input.
3. Open the artifact or source.
4. Verify one concrete item aloud.

This keeps the lesson on judgment rather than command typing.

## Six-demonstration run sheet

### 1 — Codex makes office files

- **Folder:** `/tmp/peds-ai-live-demos/01-office-files/`
- **Paste:** `PROMPT.md`
- **Inputs:** `STEM.md`
- **Open:** `family_update.docx`, `oxygen_wean_tracker.xlsx`, `noon_conference.pptx`

Verify the teaching-example sentence, six synthetic spreadsheet rows, no medication column, and placeholder rather than invented citations. If needed, run `python slides/workshops/demo1_fallback.py`.

### 2 — Codex builds a journal-club page

- **Folder:** `/tmp/peds-ai-live-demos/02-journal-club/`
- **Paste:** `PROMPT.md`
- **Only source:** `sources/OpenEvidence_systematic_review_2026.pdf`
- **Open:** `docs/index.html`, then `SOURCE_LEDGER.md`

The source is Artsi et al., article in press, DOI `10.1038/s41746-026-03077-4`. Verify the abstract’s 11 included studies on the ledger’s cited PDF viewer page. Do not publish or copy the PDF into the generated page.

### 3 — Ollama works offline

- **Folder:** `/tmp/peds-ai-live-demos/03-offline-ollama/`

```bash
ollama run qwen3.8 < demo3_ollama_prompt.txt
```

Keep Wi-Fi visibly off. The supplied synthetic H&P lacks a current weight and numeric urine output; verify that the response uses `MISSING`. If the laptop cannot run qwen3.8, substitute one already-tested 8B-class Ollama model.

### 4 — One question, three source conditions

Start a fresh Codex task in each folder:

1. `04-source-conditions/A-no-source/`
2. `04-source-conditions/B-guideline/`
3. `04-source-conditions/C-guideline-and-correction/`

Paste each folder’s `PROMPT.md`. The case is an exact, synthetic 26-day-old febrile infant with urinalysis and inflammatory markers deliberately absent. Score whether the answer names its source, locates the relevant age group, asks for missing data, handles the correction, and stays bounded.

### 5 — Codex repairs and tests a page

- **Folder:** `/tmp/peds-ai-live-demos/05-repair-page/`
- **Open first:** `broken_attendance.html`
- **Then paste:** `PROMPT.md`

Reproduce the broken interaction before the repair. After Codex edits the file, test `4`, `1`, `8`, `9`, and blank. Counts must remain `19, 22, 17, 25, 23, 20, 26, 24`; valid input highlights exactly one bar; invalid input highlights none.

### 6 — Codex builds a bounded evidence brief

- **Folder:** `/tmp/peds-ai-live-demos/06-source-packet/`
- **Paste:** `PROMPT.md` with web access off
- **Packet:** three PDFs in `sources/`, identified and hashed in `SOURCE_PACKET.md`
- **Open:** `evidence_brief.md`

The packet is the WHO 2026 discussion paper, FDA 2026 discussion paper, and Artsi et al. systematic review. Verify one table row against its PDF viewer page. The sentinel question about a pediatric randomized trial of AI-assisted lumbar-puncture decisions must begin `NOT IN PACKET`.

## Failure plan

- **Network down:** Demonstrations 1, 2, 3, 5, and 6 are entirely local. For Demonstration 4, use the already-open official AAP tabs and prepared prompts.
- **Codex build slow:** narrate the acceptance tests and open a rehearsed output; do not fill dead time with terminal output.
- **Ollama model missing:** do not download on stage. Use an already-installed smaller model or show the rehearsed output with airplane mode still visible.
- **AAP challenge page:** use the DOI tab opened before the lecture. Do not substitute an unofficial mirror live.
- **Generated claim cannot be traced:** stop at that claim. The failure is the lesson.

## Final cues

- These are demonstrations, not resident exercises.
- Codex is the working environment for five; Ollama is the offline environment for one.
- No real patient note enters any tool.
- A generated artifact is never the endpoint. Open one source, formula, file, or test before moving on.

## Theme and deployment

McLane cartoon train and BSW wordmark come from official bswhealth.com CDN assets; provenance is in [`assets/README.md`](assets/README.md). The lecture itself is deployed from [`../docs/index.html`](../docs/index.html) through GitHub Actions. Demonstration 2 creates a separate local page inside its prepared folder and never writes into this lecture’s `docs/` directory.
