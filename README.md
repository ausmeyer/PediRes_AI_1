# PediRes AI

Materials for the McLane Children’s pediatric residency hour on modern AI. Every clinical vignette and attendance count in this repository is invented.

## Ground rules

1. Do not paste names, medical record numbers, or real notes into a consumer AI product.
2. Do not copy a dose or citation until you have opened the original source yourself.
3. A model running on your laptop keeps the prompt local; it does not make the answer clinically correct or the laptop hospital-approved.

## Start here

| Need | File |
|---|---|
| Present the lecture | [`docs/index.html`](docs/index.html) |
| Read the six-demonstration runbook | [`briefing/workshops.md`](briefing/workshops.md) |
| Stage the exact prompts and inputs | [`slides/workshops/`](slides/workshops/) |
| Use the presenter cues and fallbacks | [`slides/presenter-kit.md`](slides/presenter-kit.md) |
| Read the longer research briefing | [`briefing/pediatric-resident-ai-survey.md`](briefing/pediatric-resident-ai-survey.md) |
| Trace a lecture claim to its source | [`briefing/claim-source-ledger.md`](briefing/claim-source-ledger.md) |

## Six presenter-run demonstrations

| # | Tool | Visible result | What to verify aloud |
|---:|---|---|---|
| 1 | Codex | Word, Excel, and PowerPoint files from one synthetic stem | Open all three; confirm the required teaching labels and constraints |
| 2 | Codex | A self-contained journal-club web page from one named PDF | Trace the “11 studies” claim to the PDF |
| 3 | Ollama | An offline summary of one supplied synthetic H&P | Missing weight and urine output remain `MISSING` |
| 4 | Codex | One febrile-infant question under three source conditions | Compare traceability and recognition of missing inputs |
| 5 | Codex | A repaired and tested interactive HTML page | Show the interaction issue, then run the stated acceptance tests |
| 6 | Codex | A page-cited brief from a fixed three-PDF packet | Confirm the off-corpus sentinel returns `NOT IN PACKET` |

Prepare six isolated demonstration folders from the repository root:

```bash
./slides/workshops/prepare_demo_folders.sh /tmp/peds-ai-live-demos
```

For the prebuilt Demonstration 1 fallback:

```bash
pip install -r slides/workshops/requirements.txt
python slides/workshops/demo1_fallback.py
```

## Build and publish the lecture

The Quarto source is [`slides/lecture.qmd`](slides/lecture.qmd). Render it into the GitHub Pages tree with:

```bash
cd slides
./render.sh
```

The workflow in [`.github/workflows/pages.yml`](.github/workflows/pages.yml) publishes `docs/` from `main`.
