# Presenter kit — tools, live labs, remaining holes

Companion to [`lecture.qmd`](lecture.qmd). Synthetic cases only.

## Do we need anything else before the hour?

**Need these, or the live 18 minutes fail**

| Item | Why |
|---|---|
| Your laptop on HDMI, not the podium PC as master | Cursor + Chrome + this HTML deck |
| Cursor logged in, agent mode working, **two** empty folders | Live Workshop 1 and Workshop 6 |
| `python-docx`, `openpyxl`, `python-pptx` on that laptop | Agent writes a script, or you run [`workshops/w1_fallback.py`](workshops/w1_fallback.py) / [`workshops/w6_fallback.py`](workshops/w6_fallback.py) |
| Chrome windows already logged in: consumer ChatGPT (personal), Gemini Notebook with **public** PDFs uploaded, OpenEvidence if your NPI works, **PubMed** | Live Workshops 4 and 5 |
| Frozen `lecture.html` (self-contained) + `lecture.pdf` on the laptop **and** a USB | Hospital Wi-Fi or Quarto missing |
| Printed `SYNTHETIC TEACHING CASE` tent card | Stops a well-meaning resident from offering a real H&P |

**Nice, not blocking**

- Clicker; USB-C/HDMI dongle; second screen for the Cursor terminal
- OpenEvidence access confirmed from the hospital network
- UpToDate Expert AI only if you want a fourth corpus — **not** required for W4
- Ollama `qwen3.8` pulled **only** if you add Workshop 3; it is handout, not the live hour
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

| Arm | Tool | Role |
|---|---|---|
| Presenter harness | **Cursor** Agent on `~/peds-ai-workshop/w1/` then `w6/` | Workshops 1 and 6 |
| Contrast chatbot | Consumer ChatGPT, **web search off** | Workshop 4 arm A and Workshop 5 |
| Grounded notebook | Gemini Notebook with one public AAP/CDC PDF | Workshop 4 arm B |
| Licensed RAG | OpenEvidence if NPI demo works; else skip to B-only | Workshop 4 arm C |
| Citation check | PubMed | Workshop 5 |
| Fail-safe | [`workshops/w1_fallback.py`](workshops/w1_fallback.py), [`workshops/w6_fallback.py`](workshops/w6_fallback.py) | If the agent hangs, still show files |
| This lecture | Chrome fullscreen on `lecture.html` | Everything else (`F` fullscreen, `S` speaker notes) |

**Codex / Claude Code / OpenCode:** same *kind* of thing as Cursor (model + tools + files). Keep them on the handout as the free/paid echo. Do not context-switch live unless Cursor is dead.

**Residents during the hour:** watch. The free path is in [`briefing/workshops.md`](../briefing/workshops.md). They do not need a subscription to understand the point.

### Workshop 1 — how the prompt works

Empty folder. `STEM.md` already written (synthetic bronchiolitis). In Cursor Agent:

> Read STEM.md. Create family_update.docx, oxygen_wean_tracker.xlsx, noon_conference.pptx from that stem only. No real identifiers. No medication column. No invented PMIDs. End the letter with “this is a teaching example.”

Then open the three files. Optional sting: ChatGPT-only “add the dexamethasone dose” — it will often invent a number; the spreadsheet has no meds on purpose.

If the agent stalls: `python workshops/w1_fallback.py` from this repo.

### Workshop 6 — dosing audit, same harness

Empty folder. [`KEY.md`](workshops/KEY.md) already written (fictional `teachicillin` only). In Cursor Agent:

> Read KEY.md. Create dosing.xlsx from those rules only. If KEY.md is silent, write CHECK_KEY. Add a README: not for clinical use.

Flip to formula view. The room is hunting a missing max, mg vs mcg, an adult default, or an invented frequency. If the agent hangs: `python workshops/w6_fallback.py` — that sheet omits the 400 mg cap on purpose.

### Workshop 4 — no harness required

Same febrile-infant lumbar-puncture question on three corpora. Whiteboard columns: *quoted? clickable? pediatric? would I act?*

### Workshop 5 — citation autopsy, same ChatGPT tab

Search still **off**. Paste:

> Eight Vancouver-style references on high-flow vs CPAP for bronchiolitis, 2018–2026. Include PubMed IDs.

Open PubMed on the first three identifiers. One dead or mismatched ID is enough. Do not chase all eight.

## Theme

McLane cartoon train + BSW wordmark from **official bswhealth.com CDN assets**, palette from those SVGs (`#003DA6` `#00C4B3` `#691F74` `#FF4D00` `#FFB71B`). Content slides stay paper/navy so the room still looks like noon conference, not a birthday party. Provenance: [`assets/README.md`](assets/README.md).
