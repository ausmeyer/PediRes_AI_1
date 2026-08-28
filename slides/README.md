# Slides

Residents: start at the [repository README](../README.md). This folder is the deck source.

**Source of truth:** [`lecture.qmd`](lecture.qmd) — Quarto Reveal.js, McLane train + BSW palette. Stage stack: [`presenter-kit.md`](presenter-kit.md).

```bash
cd slides
./render.sh
# Chrome fullscreen on ../docs/index.html  (F fullscreen, S speaker notes)
# Optional USB freeze with no supporting files: ./render.sh --self-contained
```

That render writes [`docs/index.html`](../docs/index.html) plus `docs/assets/` and `docs/lecture_files/` (Reveal, theme, figures). GitHub Pages: **Settings → Pages → GitHub Actions**, or **Deploy from a branch → `main` → `/docs`**. The site root is then the lecture (not the resident README). Lab 5 is a separate journal-club exercise in an empty folder; do not overwrite this `docs/` tree for that lab.

Night-before freeze: copy the `docs/` folder to the laptop **and** a PDF print (`index.html?print-pdf` in Chrome, Print → Save as PDF, landscape). `./render.sh --self-contained` is the one-file variant if you do not want a folder. PowerPoint is a fail-safe export, not a second master.

Workshop 1 and 6 fallback scripts: [`workshops/README.md`](workshops/README.md).

```bash
pip install -r workshops/requirements.txt
python workshops/lab1_fallback.py
python workshops/lab2_fallback.py
```

Brand files: [`assets/README.md`](assets/README.md). Figures: [`assets/figures/`](assets/figures/) (generated from briefing facts).
