# Presenter kit — tools, workshop order, remaining holes

Companion to [`lecture.qmd`](lecture.qmd). Synthetic cases and public sources only. Residents use the [repository README](../README.md); this file is the stage stack.

The lecture follows all eight recipes in [`briefing/workshops.md`](../briefing/workshops.md) in numerical order, then **six habits → three questions → The End / Q&A**. Backup (learning modes, attention, named timeline, parameter counts, hardware, manuscript disclosure, 2026 chronology) begins after the closing slide. Linear navigation: stop at The End.

## Do we need anything else before the hour?

**Need these, or the workshop sequence breaks**

| Item | Why |
|---|---|
| Your laptop on HDMI, not the podium PC as master | Harness + browser + this HTML deck |
| One prepared empty folder for each file-producing workshop | Keeps outputs and prompts from bleeding into one another |
| `python-docx`, `openpyxl`, `python-pptx` on that laptop | Workshop 1 fallback and the Workshop 6 spreadsheet fallback |
| GitHub account plus a public, open-access pediatric paper | Workshop 2 Pages flow |
| Ollama model downloaded and tested before arrival | Workshop 3 must still work after airplane mode |
| Browser tabs already logged in: consumer ChatGPT, Gemini Notebook with public PDFs, OpenEvidence if the NPI works, and PubMed | Workshops 4, 5, and 8 |
| Frozen `docs/` folder plus a PDF print on the laptop and a USB | Hospital Wi-Fi or Quarto missing |
| Frozen Workshop 5 model output on the USB | If the model refuses or all five PubMed IDs are valid |
| Printed `SYNTHETIC TEACHING CASE` tent card | Stops a well-meaning resident from offering a real H&P |

**Nice, not blocking**

- Clicker; USB-C/HDMI dongle; second screen for the harness terminal
- OpenEvidence access confirmed from the hospital network
- UpToDate Expert AI only if you want a fourth corpus in Workshop 4
- GME disclosure form if CME is attached
- Communications blessing if any workshop output will be posted publicly

**Not needed**

- Multiple live harnesses
- Residents installing tools while the lecture is running
- More papers for the spine (Artsi, Bergman, Grundmeier, FDA, WHO, AMA are in `briefing/papers/`)
- A second slide master in PowerPoint

Re-check on talk day: AAP dedicated AI policy, frontier model names, and product access requirements.

## What runs on stage

Use one harness consistently. Residents should see a file tree and finished artifact, not a long terminal improvisation. Keep each prompt on the clipboard.

Recurring ritual: **predict → reveal → audit**. Before each run, the room predicts what will fail. After the output appears, one resident names what they would verify.

| Tool | Workshops | Role |
|---|---|---|
| Cursor, Codex, Claude Code, or OpenCode | 1, 2, 6, 7 | Create files, run tools, and inspect outputs |
| Ollama or LM Studio | 3 | Show a synthetic note summary with the network off |
| Consumer ChatGPT, web search off | 4 and 5 | Expose ungrounded answers and citation failure |
| Gemini Notebook with public PDFs | 4, 5, and 8 | Require quotes and clickable citations from a chosen corpus |
| OpenEvidence, if available | 4 | Compare a licensed literature corpus |
| PubMed | 5 | Resolve five identifiers |
| [`workshops/lab1_fallback.py`](workshops/lab1_fallback.py) and [`workshops/lab2_fallback.py`](workshops/lab2_fallback.py) | 1 and 6 | Preserve the file and spreadsheet demonstrations if the harness hangs |
| Chrome fullscreen on `docs/index.html` | Entire lecture | `F` fullscreen; `S` speaker notes |

## Eight-workshop run sheet

### 1 — Office files from a harness

Empty folder. `STEM.md` is the synthetic bronchiolitis stem. Ask for `family_update.docx`, `oxygen_wean_tracker.xlsx`, and `noon_conference.pptx`. The tracker gets six synthetic rows and a formula for hours since the last wean attempt, but no medication column. The letter ends with “this is a teaching example.” The deck uses placeholder citations and labels them unverified. Open all three files. Fallback: `python workshops/lab1_fallback.py`.

### 2 — Journal club on GitHub Pages

Use an open-access pediatric paper or public guideline. In an empty folder, create at most eight Reveal.js slides in `docs/index.html`, plus a README and MIT license. Open the static page locally. Verify every citation before enabling Pages. If GitHub is blocked, zip the HTML and open it locally.

### 3 — Local model, airplane mode

Download and test the Ollama model before arrival. Switch to airplane mode, keep Wi-Fi visibly off, and paste only a synthetic H&P. Prompt for a problem list, overnight contingencies, and three family questions. Require `MISSING` when a value is absent. Local protects where the prompt goes; it does not certify the answer.

### 4 — One question, three systems

Ask the same febrile-infant lumbar-puncture question in three corpora: an ungrounded chatbot, Gemini Notebook with one public PDF, and OpenEvidence if available. The stem intentionally omits urinalysis and inflammatory markers. Score: *quoted? clickable? pediatric? asked for missing data? would I act?*

### 5 — Citation autopsy

With search off, ask for eight Vancouver-style bronchiolitis references with PubMed IDs. Check the first five in PubMed. Mark each: correct paper / wrong paper / missing / correct paper with the wrong year. If the model refuses or all five are valid, open the frozen rehearsal output. Then repeat in Gemini Notebook with two real PDFs and still open the citation.

### 6 — Dosing-sheet audit

Use only the fictional rules in [`workshops/KEY.md`](workshops/KEY.md): teachicillin 10 mg/kg/dose every eight hours, maximum 400 mg/dose, and `TOO_SMALL` below 2 kg. If the key is silent, the sheet must write `CHECK_KEY`. Flip to formula view and audit units, maximum, frequency, rounding, and adult defaults. Fallback: `python workshops/lab2_fallback.py`, which deliberately omits the cap.

### 7 — Harness versus chatbot

Give both tools the identical request for a single local `index.html` showing made-up noon-conference attendance. The chat arm returns code that must be copied and run. The harness arm writes, checks, and opens the file. Keep it nonclinical so the artifact cannot be mistaken for a calculator.

### 8 — Gemini Notebook

Upload four public sources. Ask a question answered by the corpus and open every citation. Ask a question outside the corpus and expect “not in sources” or a refusal. Optionally generate an audio overview. Public papers only; product privacy copy is not a hospital BAA.

## Theme

McLane cartoon train + BSW wordmark from **official bswhealth.com CDN assets**, palette from those SVGs (`#003DA6` `#00C4B3` `#691F74` `#FF4D00` `#FFB71B`). Content slides stay paper/navy so the room still looks like noon conference, not a birthday party. Provenance: [`assets/README.md`](assets/README.md). GitHub Pages for *this* lecture: [`docs/index.html`](../docs/index.html); Settings → Pages → GitHub Actions, or `main` → `/docs`. Workshop 2 uses a separate resident journal-club repo and must not overwrite this `docs/` tree.
