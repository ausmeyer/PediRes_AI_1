# Slides

Repo overview: [`../README.md`](../README.md). How to run the hour: [`presenter-kit.md`](presenter-kit.md).

**Source of truth:** [`lecture.qmd`](lecture.qmd) — Quarto Reveal.js, McLane train + BSW palette.

```bash
cd slides
quarto render lecture.qmd
# Chrome fullscreen on _site/lecture.html  (F fullscreen, S speaker notes)
```

Night-before freeze: that HTML on the laptop **and** a PDF print (`lecture.html?print-pdf` in Chrome, Print → Save as PDF, landscape). The HTML is self-contained; it does not need Google Fonts or hospital Wi-Fi. PowerPoint is a fail-safe export, not a second master.

Lab fallbacks (if Cursor hangs): [`workshops/README.md`](workshops/README.md).

```bash
pip install -r workshops/requirements.txt
python workshops/lab1_fallback.py
python workshops/lab2_fallback.py
```

Brand files: [`assets/README.md`](assets/README.md). Figures: [`assets/figures/`](assets/figures/) (generated from briefing facts; schematics labeled as such).
