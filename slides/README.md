# Slides

Residents: start at the [repository README](../README.md). This folder is the deck source.

**Source of truth:** [`lecture.qmd`](lecture.qmd) — Quarto Reveal.js, McLane train + BSW palette. Stage stack: [`presenter-kit.md`](presenter-kit.md).

```bash
cd slides
./render.sh
# or: quarto render lecture.qmd && touch ../docs/.nojekyll
# Chrome fullscreen on ../docs/index.html  (F fullscreen, S speaker notes)
```

That render writes the self-contained deck to [`docs/index.html`](../docs/index.html), which is what GitHub Pages serves. In the GitHub repo: **Settings → Pages → GitHub Actions**, or **Deploy from a branch → `main` → `/docs`**. The site root is then the lecture (not the resident README). Lab 5 is a separate journal-club exercise in an empty folder; do not overwrite this `docs/index.html` for that lab.

Night-before freeze: that HTML on the laptop **and** a PDF print (`index.html?print-pdf` in Chrome, Print → Save as PDF, landscape). The HTML is self-contained; it does not need Google Fonts or hospital Wi-Fi. PowerPoint is a fail-safe export, not a second master.

Lab 1–2 scripts: [`workshops/README.md`](workshops/README.md).

```bash
pip install -r workshops/requirements.txt
python workshops/lab1_fallback.py
python workshops/lab2_fallback.py
```

Brand files: [`assets/README.md`](assets/README.md). Figures: [`assets/figures/`](assets/figures/) (generated from briefing facts).
