# PediRes AI

Handout for the McLane Children’s pediatric residency hour on modern AI.

Cases in this repo are **invented**.

## Ground rules

1. Do not paste names, medical record numbers, or real notes into consumer ChatGPT, Claude, Gemini, or similar apps.
2. Do not copy a dose or a citation into a note until you have opened the source yourself.
3. A model on your own laptop keeps the prompt off a vendor.

## What to read

| Packet | File |
|---|---|
| The written survey | [`briefing/pediatric-resident-ai-survey.md`](briefing/pediatric-resident-ai-survey.md) |
| Step-by-step lab recipes | [`briefing/workshops.md`](briefing/workshops.md) |
| Where a number came from | [`briefing/claim-source-ledger.md`](briefing/claim-source-ledger.md) |

You do not need a paid AI subscription for any of this.

## Labs

Labs **1–4** were live. **5–8** are take-home. Full recipes are in [`briefing/workshops.md`](briefing/workshops.md).

| Lab | When | What you do |
|---|---|---|
| 1 | Live; repeat at home | Turn a fake bronchiolitis stem into Word, Excel, and PowerPoint |
| 2 | Live; repeat at home | Audit a fake dosing sheet (`teachicillin` is not a real drug) |
| 3 | Live | Same febrile-infant LP question in three tools |
| 4 | Live | Check whether ChatGPT’s PubMed IDs exist |
| 5 | Take-home | Put journal-club slides on a URL (or open a local `index.html`) |
| 6 | Take-home | Summarize a **synthetic** H&P in [Ollama](https://ollama.com) with Wi-Fi off |
| 7 | Take-home | Same file request in ChatGPT vs a harness (Cursor, OpenCode, or similar) |
| 8 | Take-home | Ask Gemini Notebook (formerly NotebookLM) over **public** PDFs only |

## Repeat Labs 1 and 2 on your laptop

[`slides/workshops/STEM.md`](slides/workshops/STEM.md) and [`slides/workshops/KEY.md`](slides/workshops/KEY.md) are written by us, not by a model.

```bash
cd slides/workshops
pip install -r requirements.txt
python lab1_fallback.py
python lab2_fallback.py
```

Lab 1 is done when three files open, the tracker has no medication column, and the letter ends with the teaching line. Lab 2 is done when you open formula view and find the missing 400 mg cap (the fallback sheet leaves it out on purpose).

Or skip the scripts: paste the stem into ChatGPT **with no identifiers**, ask for a Python script, and run that script locally.

## Take-home, in one line each

- **Lab 5.** One open paper → eight slides in `docs/index.html` → GitHub Pages, or zip the file and open it on your phone. Do not publish unverified citations.
- **Lab 6.** Install [Ollama](https://ollama.com). Pull a model that fits (`qwen3.8` or `qwen3:8b` on a small laptop). Airplane mode. Synthetic note only. Weights also live on [Hugging Face](https://huggingface.co/models).
- **Lab 7.** Ask ChatGPT for an `index.html`. Then ask a harness to write the file in an empty folder and open it.
- **Lab 8.** Upload only public papers. Click every citation. Ask something off-corpus; it should refuse.

Never use tonight’s patients, even “just the assessment.”
