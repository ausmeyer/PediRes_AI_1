# Presenter kit — tools, live blocks, remaining holes

Companion to [`lecture.qmd`](lecture.qmd). Synthetic cases only. Residents use the [repository README](../README.md); this file is the stage stack.

The live hour is **two blocks containing four lessons** (Labs 1–4), then **six takeaways → three questions → The End / Q&A**. Labs 5–8 are an appendix after questions. Backup (learning modes, attention, named timeline, parameter counts, hardware, manuscript disclosure, 2026 chronology) is after that. Linear navigation: stop at The End.

## Do we need anything else before the hour?

**Need these, or the live 18 minutes fail**

| Item | Why |
|---|---|
| Your laptop on HDMI, not the podium PC as master | Cursor + Chrome + this HTML deck |
| Cursor logged in, agent mode working, **two** empty folders | Make → inspect (Labs 1 and 2) |
| `python-docx`, `openpyxl`, `python-pptx` on that laptop | Agent writes a script, or you run [`workshops/lab1_fallback.py`](workshops/lab1_fallback.py) / [`workshops/lab2_fallback.py`](workshops/lab2_fallback.py) |
| Chrome windows already logged in: consumer ChatGPT (personal), Gemini Notebook with **public** PDFs uploaded, OpenEvidence if your NPI works, **PubMed** | Ask → verify (Labs 3 and 4) |
| Frozen `docs/` folder (or `./render.sh --self-contained`) + PDF print on the laptop **and** a USB | Hospital Wi-Fi or Quarto missing |
| Frozen Lab 4 ChatGPT output on the USB | If the live model refuses or all three PubMed IDs are valid, inspect the saved example |
| Printed `SYNTHETIC TEACHING CASE` tent card | Stops a well-meaning resident from offering a real H&P |

**Nice, not blocking**

- Clicker; USB-C/HDMI dongle; second screen for the Cursor terminal
- OpenEvidence access confirmed from the hospital network
- UpToDate Expert AI only if you want a fourth corpus — **not** required for Lab 3
- Ollama `qwen3.8` pulled **only** if you add Lab 6; it is handout, not the live hour
- GME disclosure form if CME is attached
- Communications blessing if this HTML will be **public** GitHub Pages (train mark is trademarked)

**Not needed**

- Codex as a second live harness
- Residents installing Cursor during the hour
- More papers for the spine (Artsi, Bergman, Grundmeier, FDA, WHO, AMA are in `briefing/papers/`)
- A second slide master in PowerPoint

Re-check on talk day (facts that move): GLM-5.3 weights, AAP dedicated AI policy, frontier prices.

## What runs on stage

**One harness. Cursor.**

You are already in it. Residents see a file tree, not a black terminal. Paste a canned prompt. Do not live-compose a 200-word prompt while they watch.

Recurring ritual on every demo: **predict → reveal → audit**. Before you paste, the room predicts what will fail. After the artifact is on the projector, one resident names the check they would perform.

| Arm | Tool | Role |
|---|---|---|
| Presenter harness | **Cursor** Agent on `~/peds-ai-workshop/lab1/` then `lab2/` | Make → inspect |
| Contrast chatbot | Consumer ChatGPT, **web search off** | Lab 3 arm A and Lab 4 |
| Grounded notebook | Gemini Notebook with one public AAP/CDC PDF | Lab 3 arm B |
| Licensed RAG | OpenEvidence if NPI demo works; else skip to B-only | Lab 3 arm C |
| Citation check | PubMed | Lab 4 |
| Fail-safe | [`workshops/lab1_fallback.py`](workshops/lab1_fallback.py), [`workshops/lab2_fallback.py`](workshops/lab2_fallback.py) | If the agent hangs, still show files |
| This lecture | Chrome fullscreen on `docs/index.html` | Everything else (`F` fullscreen, `S` speaker notes) |

**Codex / Claude Code / OpenCode:** same *kind* of thing as Cursor (model + tools + files). Keep them on the handout as the free/paid echo. Do not context-switch live unless Cursor is dead.

**Residents during the hour:** watch. The free path is in [`briefing/workshops.md`](../briefing/workshops.md). They do not need a subscription to understand the point.

### Make → inspect (Labs 1 and 2)

Stay in Cursor. Do not bounce to the browser until both files exist.

**Lab 1 — files from a harness.** Empty folder. `STEM.md` already written (synthetic bronchiolitis — we wrote it; it is not model output). Prompt is on the clipboard, not the projector:

> Read STEM.md. Create family_update.docx, oxygen_wean_tracker.xlsx, noon_conference.pptx from that stem only. No real identifiers. No medication column. No invented PMIDs. End the letter with “this is a teaching example.”

Then open the three files. Optional sting: ChatGPT-only “add the dexamethasone dose” — it will often invent a number; the spreadsheet has no meds on purpose.

If the agent stalls: `python workshops/lab1_fallback.py` from this repo.

**Lab 2 — spot the bug.** Same harness, new folder. Show the formula (`=B2*10`, no cap) **before** you name the error list. [`KEY.md`](workshops/KEY.md) already written (fictional `teachicillin` only). Paste:

> Read KEY.md. Create dosing.xlsx from those rules only. If KEY.md is silent, write CHECK_KEY. Add a README.

Flip to formula view. The room is hunting a missing max, mg vs mcg, an adult default, or an invented frequency. If the agent hangs: `python workshops/lab2_fallback.py` — that sheet omits the 400 mg cap on purpose.

### Ask → verify (Labs 3 and 4)

Stay in the browser.

**Lab 3 — one question, three corpora.** Same febrile-infant lumbar-puncture question. The stem is **missing urinalysis and inflammatory markers on purpose.** Whiteboard: *quoted? clickable? pediatric? did it ask for missing data? would I act?*

**Lab 4 — citation autopsy.** Search still **off**. Paste:

> Eight Vancouver-style references on high-flow vs CPAP for bronchiolitis, 2018–2026. Include PubMed IDs.

Open PubMed on the first three identifiers. One dead or mismatched ID is enough. Do not chase all eight. If the live model refuses or all three IDs are valid, say “good behavior today” and open the frozen rehearsal file. Do not invent PubMed IDs.

Labs 5–8 (Pages, Ollama, harness loop, Gemini Notebook) are take-home. They live after Q&A. Do not run them live.

## Take-home, after Q&A

Each of Labs 5–8 is a short projector card. Point, do not demo. Recipes stay in [`briefing/workshops.md`](../briefing/workshops.md).

- **Lab 5:** paper → eight slides → verify → share (GitHub Pages or a local zip).
- **Lab 6:** airplane mode, synthetic data, hardware limits. Install commands in the written recipe.
- **Lab 7:** same `index.html` request in ChatGPT vs a harness. Nonclinical artifact: synthetic noon-conference attendance, not a growth z-score.
- **Lab 8:** source-grounded notebook over public PDFs. Product rename (NotebookLM → Gemini Notebook) is in the handout.

## Theme

McLane cartoon train + BSW wordmark from **official bswhealth.com CDN assets**, palette from those SVGs (`#003DA6` `#00C4B3` `#691F74` `#FF4D00` `#FFB71B`). Content slides stay paper/navy so the room still looks like noon conference, not a birthday party. Provenance: [`assets/README.md`](assets/README.md). GitHub Pages for *this* lecture: [`docs/index.html`](../docs/index.html); Settings → Pages → GitHub Actions, or `main` → `/docs`. Lab 5 is a resident journal-club repo, not that file.
