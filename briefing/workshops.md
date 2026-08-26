# Workshop recipes: from-scratch demos for pediatric residents

Companion to [`pediatric-resident-ai-survey.md`](pediatric-resident-ai-survey.md).  
**All cases are synthetic. No PHI.**

**Design.** Each recipe starts from an **empty folder** (or empty notebook). Each has a presenter path (you may use a paid harness) and a **resident-replicable free path**. Most residents have no subscription and have never used a harness. Hospital Wi-Fi may block model downloads, GitHub, or local servers; have a USB copy of weights and a local HTML deck as fallback.

**Lecture numbering.** Live hour is Labs 1–4, in this order. Take-home is Labs 5–8. Older “Workshop N” headings in this file are the recipes; the live labels on the slides win. Residents repeating Labs 1–2 at home can use [`../slides/workshops/`](../slides/workshops/README.md).

| Lab | When | What | Recipe in this file |
|---|---|---|---|
| 1 | Live | Office files from a harness | Workshop 1 |
| 2 | Live | Dosing-sheet audit | Workshop 6 |
| 3 | Live | One question, three corpora | Workshop 4 |
| 4 | Live | Citation autopsy | Workshop 5 |
| 5 | Take-home | GitHub Pages journal club | Workshop 2 |
| 6 | Take-home | Local Ollama | Workshop 3 |
| 7 | Take-home | Harness loop vs chatbot | Workshop 7 |
| 8 | Take-home | Gemini Notebook | Workshop 8 |

**Shared setup (2 minutes, once).**

- Label the projector: `SYNTHETIC TEACHING CASE — NOT A REAL PATIENT`.
- Disable any browser extensions that auto-upload pages.
- If using a cloud model, confirm the account is **not** receiving PHI.
- Working directory: `~/peds-ai-workshop/` (empty).

---

## Workshop 1 — Office files without Microsoft 365

**Time (live):** 10–12 minutes  
**Goal:** Produce a real Word letter, Excel tracker, and PowerPoint noon-conference deck from a synthetic bronchiolitis admission.  
**Surprising artifact:** Three files residents can open on their phones.  
**HIPAA:** Synthetic only. Still do not use a consumer cloud account as a habit for real notes.

### Synthetic stem (read aloud)

> 6-month-old former 36-week infant, day 2 of RSV bronchiolitis, SpO2 nadir 88% on RA overnight, now 94% on 0.5 L NC. Taking 50% of feeds. No underlying cardiopulmonary disease. Family wants a plain-language update and the team wants a wean tracker for tonight’s cross-cover.

### Presenter path (harness)

Empty folder. In Claude Code, Codex, Cursor, or OpenCode:

> Create three files in this folder from the synthetic stem in STEM.md (I will paste it). Do not add any real identifiers.
> 1. `family_update.docx` — 1-page family letter, 6th-grade reading level, no dose recommendations, ends with “this is a teaching example.”
> 2. `oxygen_wean_tracker.xlsx` — columns: datetime, SpO2, NC L/min, work of breathing (0–3), feeds %, comments. Pre-fill 6 synthetic rows. Add a formula for hours since last wean attempt.
> 3. `noon_conference.pptx` — 8 slides: title, objectives, pathophysiology cartoon-level, evidence bullets with PLACEHOLDER citations (not invented PMIDs), wean principles, discharge criteria, take-home, references slide that says “citations not yet verified.”

If the harness has **Skills** for docx/xlsx/pptx (Claude’s document skills; or `python-docx` / `openpyxl` / `python-pptx` in the environment), let it run. If not, ask it to write a `build_files.py` and execute it.

### Resident free path

1. Install Python 3 if needed.  
2. `pip install python-docx openpyxl python-pptx`  
3. Paste the stem into ChatGPT **without identifiers** and ask for a **Python script**, not the medical advice.  
4. Run the script locally. Open files in Google Drive, LibreOffice, or Word Preview.

### Intentional failure to show

Ask the model (chat-only, no files) to “add the standard dexamethasone dose for this infant.” It will often invent a number. Contrast with the spreadsheet, which has **no medication column on purpose**.

### Teaching point

Chatbots return paragraphs. Harnesses return **artifacts you can version and audit**. Anthropic’s Skills post (16 Oct 2025) is explicit that skills can include executable code for Excel/PowerPoint/Word rather than relying on token generation alone.

---

## Workshop 2 — Journal club on GitHub Pages, no coding by the resident

**Time (live):** 8–10 minutes  
**Goal:** Markdown slides → Reveal.js (or similar static HTML) → GitHub repo → public URL.  
**Surprising artifact:** A shareable link that works on a phone in the back row.  
**HIPAA:** Public repo. Only synthetic or published, cited material.

### Stem

Use a **published** open-access pediatric paper (for example a CDC/AAP open guideline PDF or a Creative Commons review). Do not upload a paywalled PDF you do not have rights to post.

### Presenter path

Empty folder:

> Build a Reveal.js slide deck in `docs/index.html` (or `index.html` at repo root for GitHub Pages) summarizing PAPER.md. Eight slides max. Include a QR-ready URL placeholder. Add a MIT license and a README that says this is a teaching fork.

Then:

```bash
git init
git add .
git commit -m "Add synthetic journal club deck"
# create a public GitHub repo and push
# Settings → Pages → deploy from main / docs
```

### Resident free path

- No GitHub account: zip the `index.html` and open locally.  
- No git knowledge: GitHub web UI “Upload files” into a new public repo, enable Pages.  
- Alternative: Marp / Slidev if the presenter prefers Markdown-only; the lesson is **static hosting**, not a particular framework.

### Intentional failure

Show a model-written “References” slide with a plausible but **unverified** DOI. Do not enable Pages until Workshop 5’s lesson is stated: **no invented citations on a public URL.**

### Teaching point

Versioned teaching materials beat emailing `final_v7.pptx`. “I don’t code” is not a blocker if an agent writes the HTML once.

---

## Workshop 3 — Air-gapped local model (zero vendor)

**Time (live):** 10 minutes (plus pre-download)  
**Goal:** Summarize a synthetic H&P with Ollama while the laptop is in airplane mode.  
**Surprising artifact:** A competent summary with the network off.  
**HIPAA:** This is the closest “no vendor BA” demo. Still not a licensed hospital system. Do not use real notes.

### Hardware honesty (say this before you boot)

| Machine | Realistic local model | Not realistic |
|---|---|---|
| Mac Studio / 32 GB unified or 24 GB NVIDIA | Qwen3.8-27B Q4 (~18 GB) or Muse Glimmer 30B Q4 | Full BF16 30B |
| 16 GB RAM laptop, no GPU | 8B-class GGUF, slow | 27B at usable speed |
| Typical resident Windows 8–16 GB | 3B–8B quantized | Anything “frontier local” |

Ollama library listing for `qwen3.8` (retrieved 25 Aug 2026): 18 GB, 256K context, text+image, `ollama run qwen3.8`. Meta’s Glimmer post: 4-bit under ~20 GB targeting 24/32 GB GPUs.

### Presenter path (pre-work the night before)

```bash
# online, once
ollama pull qwen3.8          # or a documented 8B fallback: ollama pull qwen3:8b
# verify
ollama run qwen3.8 "Reply with the word OFFLINE_OK"
```

Day of:

1. Airplane mode.  
2. Paste `synthetic_hp.txt` (no real names).  
3. Prompt: “List problems, overnight contingencies, and three questions for the family. Do not invent labs that are not in the note. If a value is missing, say MISSING.”  
4. Show System Settings / Wi-Fi off the whole time.

### Resident free path

Install Ollama from https://ollama.com (or LM Studio). Pull the largest model that **fits**. Alternatives: llama.cpp + GGUF; LM Studio GUI.

### Intentional failure

While **online**, paste the same note into consumer ChatGPT. Ask the room: “Which of these just created a business associate we do not have a contract with?” (Answer: the cloud one, if the note were PHI.)

### Teaching point

Local models are a **privacy architecture**, not a quality trophy. Offline Qwen3.8-27B is useful for drafting. It is not GPT-5.6 Sol. Unmanaged laptops still get stolen.

---

## Workshop 4 — Same question, three systems

**Time (live):** 12 minutes  
**Goal:** One pediatric question, three corpora.  
**Surprising artifact:** Side-by-side citations: fabricated vs quoted vs editorial.  
**HIPAA:** Public sources only. No patient detail.

### Question (from a published teaching case pattern, not a real child)

> In a previously healthy 8-week-old with fever of 38.5 °C, well-appearing, what is the current AAP guidance on lumbar puncture? Quote the document. If you cannot quote, say you cannot.

### Three systems

| Arm | System | Corpus |
|---|---|---|
| A | Consumer LLM, **web search off** | Parameters only |
| B | Gemini Notebook (formerly NotebookLM) | **One** public AAP or CDC PDF you uploaded |
| C | OpenEvidence (if NPI demo available) or, if not, PubMed Central full text pasted into Notebook | Licensed journals / your PDF |

### Procedure

1. Run A. Highlight any guideline-sounding sentence. Demand a PMID/DOI. Try to open it.  
2. Run B. Require a quote with page/section. Click the citation chip.  
3. Run C if available. Click through to the partner journal.  
4. Score on a whiteboard: *quoted? clickable? pediatric-specific? would I act?*

### Intentional failure

Arm A will often emit a confident 2021-vs-2021 febrile infant algorithm mashup with a real-looking citation.

### Teaching point

RAG is a **corpus choice**. OpenEvidence ≠ UpToDate ≠ ChatGPT. Artsi et al. 2026 found OpenEvidence generally better on fabricated citations than general LLMs **in studies that measured that**, and still methodologically thin. Do not overclaim.

---

## Workshop 5 — Citation autopsy

**Time (live hour):** 4 minutes (full recipe 8)  
**Goal:** Verify five identifiers from a model-written reference list.  
**Surprising artifact:** At least one dead or mismatched citation in a fluent list (very often).  
**HIPAA:** None.

### Prompt (ungrounded model)

> Give eight Vancouver-style references on pediatric high-flow nasal cannula vs CPAP for bronchiolitis, 2018–2026. Include PMIDs.

### Resident task (pairs, 4 minutes)

For references 1–5:

1. Open PubMed.  
2. Search the PMID.  
3. Mark: exists / exists-but-wrong-paper / does not exist / correct paper but wrong year.

### Presenter closer

Re-run the same prompt in Gemini Notebook with **two real PDFs** uploaded. Show that grounded mode still requires a click—models mis-attribute real papers.

### Teaching point

ICMJE: authors must ensure attribution of quoted material and that AI text is not plagiarized or fabricated ([ICMJE Recommendations](https://www.icmje.org/icmje-recommendations.pdf)). The autopsy is how you operationalize that sentence.

---

## Workshop 6 — Spreadsheet that looks official and can harm if trusted

**Time (live hour):** 5 minutes (full recipe 10)  
**Goal:** Agent builds a weight-based dosing sheet; residents audit every formula.  
**Surprising artifact:** A pretty Excel file with at least one wrong formula or unit.  
**HIPAA:** Synthetic weights only. **No live administration.**

### Guardrails (read first)

This is an **audit exercise**, not a formulary. Use a **fictional** drug name (`teachicillin`) or a widely published OTC example with a **labeled answer key** you prepared. Do **not** generate a real hospital gentamicin nomogram from a model and do not leave it on a shared drive.

### Answer key (presenter prepares on paper)

Example teaching key (synthetic):

- `teachicillin` oral: 10 mg/kg/dose (max 400 mg/dose) every 8 hours  
- Spreadsheet must use `=weight_kg*10` and cap with `=MIN(weight_kg*10,400)`  
- Must refuse weights < 2 kg with a warning cell

### Presenter path

> Create dosing.xlsx with inputs: weight_kg, age_months. Compute teachicillin_mg_per_dose and doses_per_day using ONLY the rules in KEY.md. If KEY.md is silent, write CHECK_KEY rather than guessing. Add a README: “Not for clinical use.”

Then flip the projector to formula view. Residents find:

- mg vs mcg,
- missing max,
- adult default,
- `round()` that always rounds up,
- hallucinated frequency.

### Teaching point

Numeric hallucination plus official formatting is how a model kills someone. FDA’s discussion paper uses an **insulin-dose** example as higher-consequence than OTC hydrocortisone ([FDA CDRH 2026](https://www.fda.gov/)). Same geometry: action-directing plus high harm.

---

## Workshop 7 — Harness vs chatbot (the loop is the product)

**Time (live):** 8–10 minutes  
**Goal:** Same request in ChatGPT paste vs an agent in an empty git repo.  
**Surprising artifact:** A running local HTML growth-chart **teaching toy** (synthetic data) vs a blob of code that does not run.  
**HIPAA:** Synthetic points only. Not a clinical growth chart for a real child.

### Request (identical in both arms)

> In an empty folder, create a single `index.html` that plots WHO-style weight-for-age **synthetic** curves for 0–24 months and lets me type a weight to see a labeled teaching z-score **using an explicit formula in a comment**. No external APIs. Then run a basic check that the file opens.

### Arm A — Chatbot

Paste into consumer ChatGPT. Try to copy files by hand. Watch the room stall on “where do I put this.”

### Arm B — Harness

Claude Code / Codex / Cursor / OpenCode / `ollama launch opencode --model qwen3.8`:

> Implement the request. Open a local server if needed. Do not use real patient data.

Codex sandbox talking point: default workspace-write, network off unless enabled ([OpenAI Codex sandbox docs](https://developers.openai.com/codex/concepts/sandboxing)).

### Teaching point

The product residents should learn is the **loop** (files, tools, tests), not the chat box. Paid Cursor is optional; OpenCode + Ollama is the free echo.

---

## Workshop 8 — Gemini Notebook as a research notebook

**Time (live):** 8 minutes  
**Goal:** Four public sources → grounded Q&A ± audio/slide overview.  
**Surprising artifact:** Questions that cite **your** PDFs.  
**HIPAA:** Google’s “we don’t train on your uploaded data” (Workspace product copy) is **not** a hospital BAA. Public papers only.

### Sources (examples)

- AAP digital-ecosystems policy PDF (2026)  
- Grundmeier et al. 2026 *Pediatrics* SOTA review (in `briefing/papers/`; **not** AAP policy)  
- ICMJE Recommendations PDF  
- CDC/AAP open bronchiolitis or immunization page saved as PDF  
- Artsi et al. 2026 OpenEvidence review (open access; local PDF in `briefing/papers/`)

### Procedure

1. Create a notebook. Upload only those files.  
2. Ask: “What does AAP say it is **not** covering in this statement regarding AI?” (Answer: dedicated AI policy is forthcoming.) Contrast with Grundmeier 2026: useful counseling review, **not** that policy.  
3. Ask a question **outside** the corpus. The right behavior is refusal or “not in sources.”  
4. Optional: generate an audio overview for commute learning.

Rename note: NotebookLM became **Gemini Notebook** on 16 July 2026; secure cloud computer (code execution) is tier-gated ([Google 2026](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)).

### Teaching point

Source-grounded notebooks are the right tool for **journal club and policy**, not for the census.

---

## Optional ninth — Disclosure quiz (2 minutes)

Dummy cover letter. Which uses must be reported under *Pediatrics* / ICMJE?

| Use | Report? |
|---|---|
| Grammar in ChatGPT | Yes (writing assistance → Acknowledgments + cover letter) |
| Model generated a figure | Yes (Methods + cover letter; name tool and manufacturer) |
| Spellcheck in Word | Generally no (routine; COPE/CASRAI-style distinction) |
| Model listed as co-author | Never |
| Model invented three PMIDs you kept | Report **and** you have a bigger problem |

---

## Hospital-network fallback kit

Pre-load on a USB drive:

- `qwen3.8` GGUF or Ollama blob (if license permits redistribution internally; otherwise each laptop pulls at home)  
- Workshop 1 Python script already run, with output files  
- Workshop 2 `index.html`  
- PDFs for Workshops 4 and 8  
- This file and the briefing, printed

If GitHub is blocked, skip Pages and open HTML locally. If Python is blocked, run Workshop 1 outputs from the USB.

---

## Facilitator checklist

- [ ] Synthetic banner on every slide and terminal  
- [ ] No Epic, no email with real names, no photo of a child  
- [ ] Four live demos in the hour (Labs 1, 2, 3, 4); 18 minutes on the clock  
- [ ] Hardware story for Lab 6 (Ollama) told only if someone asks; it is take-home  
- [ ] Lab 2 answer key on paper, not generated live as “truth”  
- [ ] Handout QR to this markdown (or PDF export)
