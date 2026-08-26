# Slides

**Source of truth:** [`lecture.qmd`](lecture.qmd) — Quarto Reveal.js, visual-first, McLane train + BSW palette.  
**How to run the hour:** [`presenter-kit.md`](presenter-kit.md).  
**Brand files:** [`assets/README.md`](assets/README.md).  
**Figures:** [`assets/figures/`](assets/figures/) (generated from briefing facts; schematics labeled as such).

```bash
cd slides
quarto render lecture.qmd
# open _site/lecture.html in Chrome, fullscreen
```

Night-before freeze: that HTML on the laptop **and** a PDF print of the deck (`lecture.html?print-pdf` in Chrome, Print → Save as PDF, landscape). PowerPoint is a fail-safe export, not the master. The HTML is self-contained; it does not need Google Fonts or hospital Wi-Fi.

Workshop 1 fallback (if Cursor hangs): `python workshops/w1_fallback.py` (needs `python-docx`, `openpyxl`, `python-pptx`; see [`workshops/requirements.txt`](workshops/requirements.txt)).

**Why Reveal, not PowerPoint as master.** The hour is also the teaching object for Workshop 2 (Markdown → static HTML). Quarto keeps the deck in git next to the briefing. Hospital podium reality still wants a PDF (and a `.pptx` export if GME demands Office). Do not maintain a second slide master.
