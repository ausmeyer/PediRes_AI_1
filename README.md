# PediRes AI

One-hour workshop-lecture for pediatric residents at McLane Children’s Hospital (Temple). A survey of modern AI, then four live labs.

Teaching cases are **synthetic**. This is not a clinical protocol and not patient-specific medical direction.

## Start here

| You want to… | Open |
|---|---|
| Give the hour | [`slides/presenter-kit.md`](slides/presenter-kit.md) |
| Edit or render the deck | [`slides/lecture.qmd`](slides/lecture.qmd) |
| Read the packet | [`briefing/pediatric-resident-ai-survey.md`](briefing/pediatric-resident-ai-survey.md) |
| Run a lab from scratch | [`briefing/workshops.md`](briefing/workshops.md) |
| Check a factual claim | [`briefing/claim-source-ledger.md`](briefing/claim-source-ledger.md) |

## Give the hour

```bash
cd slides
quarto render lecture.qmd
```

Open `_site/lecture.html` in Chrome, fullscreen (`F`). Speaker notes: `S`. Freeze that HTML and a PDF print (`lecture.html?print-pdf`) on the laptop and a USB the night before. The HTML is self-contained; hospital Wi-Fi is not required.

Live labs are **1–4**. Take-home is **5–8**. If Cursor hangs:

```bash
cd slides
pip install -r workshops/requirements.txt
python workshops/lab1_fallback.py
python workshops/lab2_fallback.py
```

## What’s in the repo

```
slides/      Reveal deck, McLane theme, lab fallbacks
briefing/    Survey, workshop recipes, claim ledger, source PDFs
```

The train mark is BSW / McLane Children’s. Internal teaching use.

Figures are generated from briefing facts:

```bash
cd slides && python3 assets/generate_figures.py
```

Needs matplotlib and numpy. Schematics on the canvas are labeled as cartoons, not measured models.
