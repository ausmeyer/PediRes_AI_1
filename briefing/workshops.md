# Live demonstrations: presenter runbook for pediatric residents

Companion to [`pediatric-resident-ai-survey.md`](pediatric-resident-ai-survey.md).

**Every clinical vignette is synthetic. No PHI. These are demonstrations, not clinical protocols.**

## What changed

The lecture now contains six short, presenter-run demonstrations. Demonstrations 1, 2, 4, 5, and 6 run in **Codex**. Demonstration 3 runs in **Ollama** with the laptop offline. There is no participant setup or alternate editor path.

| Demonstration | Tool | Visible result |
|---|---|---|
| 1 | Codex | Word, Excel, and PowerPoint files from one synthetic stem |
| 2 | Codex | A self-contained journal-club web page from one named PDF |
| 3 | Ollama | An offline summary of one provided synthetic H&P |
| 4 | Codex | The same clinical question under three explicit source conditions |
| 5 | Codex | A repaired, tested interactive HTML page |
| 6 | Codex | A page-cited evidence brief from one fixed three-PDF packet |

## One-time preparation

From the repository root, create six clean demonstration folders:

```bash
./slides/workshops/prepare_demo_folders.sh /tmp/peds-ai-live-demos
```

The script refuses to overwrite an existing directory. Use a new destination for each rehearsal. It copies every input into the folder where it will be used, including the exact PDFs for Demonstrations 2 and 6.

Before residents arrive:

- Put `SYNTHETIC TEACHING CASE — NOT A REAL PATIENT` on the projector.
- Open this runbook and [`../slides/presenter-kit.md`](../slides/presenter-kit.md).
- Open Codex on `/tmp/peds-ai-live-demos`.
- Pull and test the Ollama model while online: `ollama pull qwen3.8`.
- Open the two official AAP links in Demonstration 4 once; the AAP site may challenge a new browser session.
- Keep a local copy of the lecture and the prepared demonstration folders on the teaching laptop.

Use the same delivery rhythm each time: **name the practical job → run the exact prompt → open the artifact or source → verify one thing aloud**. These are demonstrations of possibilities residents might consider.

---

## Demonstration 1 — Codex makes files, not paragraphs

- **Time:** 5 minutes
- **Working folder:** `/tmp/peds-ai-live-demos/01-office-files/`
- **Inputs supplied:** `STEM.md`, `PROMPT.md`
- **Expected outputs:** `family_update.docx`, `oxygen_wean_tracker.xlsx`, `noon_conference.pptx`

### Run it

1. Open the folder in Codex.
2. Paste the complete contents of `PROMPT.md`.
3. Let Codex create and inspect all three files.
4. Open each artifact, not just the terminal output.

### Verify aloud

- The letter ends with “This is a teaching example.”
- The tracker has six synthetic rows and **no medication column**.
- The slides label citations as placeholders rather than inventing PMIDs or DOIs.

### If the live build stalls

From `slides/workshops/`, run `python demo1_fallback.py` and open the three files in `demo1_out/`.

### Teaching point

Codex can create inspectable files. A polished file is still only a draft until a person verifies its claims against sources, formulas against rules, and citations against originals.

---

## Demonstration 2 — Codex builds a journal-club page from one exact PDF

- **Time:** 6 minutes
- **Working folder:** `/tmp/peds-ai-live-demos/02-journal-club/`
- **Input supplied:** `sources/OpenEvidence_systematic_review_2026.pdf`
- **Prompt supplied:** `PROMPT.md`

### Source

Artsi Y, Sorin V, Glicksberg BS, et al. *OpenEvidence clinical question-answering platform: systematic review of early evaluations.* **npj Digital Medicine.** Article in press; accepted July 26, 2026. DOI: [`10.1038/s41746-026-03077-4`](https://doi.org/10.1038/s41746-026-03077-4). The supplied accepted manuscript is licensed CC BY-NC-ND 4.0.

### Run it

1. Open the folder in Codex and paste `PROMPT.md`.
2. Let Codex build `docs/index.html`, `README.md`, and `SOURCE_LEDGER.md`.
3. Open `docs/index.html` locally and move through all seven sections.
4. Open one numeric claim in `SOURCE_LEDGER.md`, then jump to that PDF viewer page.

The prompt forbids outside browsing, copied figures, invented identifiers, and external JavaScript libraries. It also requires the page to say that the PDF is an accepted manuscript, not the final typeset article.

### Verify aloud

The abstract reports 11 included studies. Confirm that number in the source before admiring the page.

### Teaching point

The useful chain is **named source → generated artifact → page-level verification**. The HTML is portable; the truth still lives in the paper.

---

## Demonstration 3 — Ollama summarizes a provided H&P offline

- **Time:** 5 minutes
- **Working folder:** `/tmp/peds-ai-live-demos/03-offline-ollama/`
- **Input and prompt supplied together:** `demo3_ollama_prompt.txt`

### Run it

Show Wi-Fi off, then run:

```bash
cd /tmp/peds-ai-live-demos/03-offline-ollama
ollama run qwen3.8 < demo3_ollama_prompt.txt
```

If the teaching laptop cannot run `qwen3.8`, rehearse and substitute an already-downloaded 8B-class Ollama model. Change only the model name in the command; do not change the prompt.

### Verify aloud

- The note explicitly omits a current weight and numeric urine output.
- The response should write `MISSING` for those facts, not infer them.
- Local execution controls where the prompt goes; it does not prove that the clinical summary is correct.

### Teaching point

Airplane mode makes data flow visible. It does not make the model a hospital policy, a medical device, or a source of truth.

---

## Demonstration 4 — One question, three source conditions in Codex

- **Time:** 7 minutes
- **Parent folder:** `/tmp/peds-ai-live-demos/04-source-conditions/`
- **Synthetic case:** a term, well-appearing 26-day-old infant with rectal temperature 38.5 °C; urinalysis and inflammatory markers are deliberately missing.

Use three fresh Codex tasks so an earlier source cannot leak into a later answer.

| Condition | Folder | What Codex may use |
|---|---|---|
| A | `A-no-source/` | `CASE.md` only; no web and no other files |
| B | `B-guideline/` | `CASE.md` plus the exact AAP guideline link in `SOURCES.md` |
| C | `C-guideline-and-correction/` | `CASE.md` plus the guideline and its correction in `SOURCES.md` |

### Exact sources

- Pantell RH, Roberts KB, Adams WG, et al. *Evaluation and Management of Well-Appearing Febrile Infants 8 to 60 Days Old.* **Pediatrics.** 2021;148(2):e2021052228. DOI: [`10.1542/peds.2021-052228`](https://doi.org/10.1542/peds.2021-052228).
- *Statement of Correction* for that guideline. **Pediatrics.** 2021;148(5):e2021054063. DOI: [`10.1542/peds.2021-054063`](https://doi.org/10.1542/peds.2021-054063).

### Run it

For A, B, then C: open the named folder, start a fresh Codex task, and paste its `PROMPT.md`. Do not add laboratory values that are not in `CASE.md`.

Score each answer on five questions:

1. Did it state what source material it actually used?
2. Did it quote or point to the relevant age-specific recommendation?
3. Did it ask for the missing urinalysis and inflammatory markers?
4. In C, did it determine whether the correction changes the conclusion?
5. Did it keep the answer educational rather than pretending to manage a patient?

### Expected contrast

Condition A should be cautious and should not fabricate a quotation. B should distinguish a recommendation that depends on source and age group. C should explicitly account for the correction. The correct demonstration outcome is not a particular sentence—it is better traceability and better recognition of missing inputs.

### Teaching point

Retrieval is a source choice. Giving the same model a defined corpus changes what can be traced back to an original source.

---

## Demonstration 5 — Codex repairs and tests a broken page

- **Time:** 5 minutes
- **Working folder:** `/tmp/peds-ai-live-demos/05-repair-page/`
- **Inputs supplied:** `broken_attendance.html`, `PROMPT.md`

The page contains made-up noon-conference attendance counts for eight weeks. It is intentionally broken: typing a week does not highlight the matching bar.

### Run it

1. Open `broken_attendance.html` first and show the interaction issue.
2. Tell the room that the data are visible but the week-selection interaction does not respond.
3. Open the folder in Codex and paste `PROMPT.md`.
4. Let Codex inspect, edit, and test the existing file.
5. Enter `4`: only Week 4 should turn orange. Enter `9`: no bar should be highlighted and the page should ask for 1–8.

### Acceptance tests already in the prompt

- No console error on load.
- Weeks and counts remain `1–8` and `19, 22, 17, 25, 23, 20, 26, 24`.
- Valid input highlights exactly one bar.
- Invalid input highlights none and displays `Enter a week from 1 to 8.`
- No external APIs, libraries, or network requests.

### Teaching point

The loop is the product: reproduce, inspect, edit, run, and verify. Codex is most useful when it can work on the artifact itself.

---

## Demonstration 6 — Codex produces a source-bounded evidence brief

- **Time:** 6 minutes
- **Working folder:** `/tmp/peds-ai-live-demos/06-source-packet/`
- **Inputs supplied:** `PROMPT.md`, `SOURCE_PACKET.md`, and three PDFs in `sources/`

### Exact packet

1. World Health Organization. *Artificial intelligence and evidence-informed policy – emerging challenges and opportunities: discussion paper.* Geneva: WHO; 2026. DOI: [`10.2471/B09667`](https://doi.org/10.2471/B09667). CC BY-NC-SA 3.0 IGO.
2. U.S. Food and Drug Administration, Center for Devices and Radiological Health. *Considerations for the Regulation of Generative AI-Enabled Medical Devices: Discussion Paper and Request for Feedback.* 2026. Docket [`FDA-2026-N-7874`](https://www.regulations.gov/docket/FDA-2026-N-7874).
3. Artsi Y, Sorin V, Glicksberg BS, et al. *OpenEvidence clinical question-answering platform: systematic review of early evaluations.* **npj Digital Medicine.** Article in press; accepted July 26, 2026. DOI: [`10.1038/s41746-026-03077-4`](https://doi.org/10.1038/s41746-026-03077-4). CC BY-NC-ND 4.0.

### Run it

1. Turn Codex web access off for this task.
2. Paste `PROMPT.md`.
3. Open the generated `evidence_brief.md`.
4. Pick one row and verify the quoted idea on the cited PDF viewer page.
5. Read the sentinel answer aloud. The packet contains no pediatric randomized trial of AI-assisted lumbar-puncture decisions, so the answer must be `NOT IN PACKET`.

### Verify aloud

The brief must distinguish a systematic review from two discussion papers and must not convert any of them into clinical guidance.

### Teaching point

A fixed packet can make synthesis more inspectable. It cannot make absent pediatric evidence appear.

---

## Presenter fallback kit

Keep these on the teaching laptop, not scattered across cloud tabs:

- the prepared `/tmp/peds-ai-live-demos/` folder;
- the already-rendered Demonstration 1 outputs from `demo1_fallback.py`;
- the Ollama model verified before airplane mode;
- the three local PDFs for Demonstration 6;
- the exact AAP guideline and correction links open in browser tabs;
- the lecture at `docs/index.html`.

If the network fails, Demonstrations 1, 2, 3, 5, and 6 still run locally. For Demonstration 4, explain the three source conditions from the prepared prompts and use the already-open AAP tabs; do not substitute an unofficial mirror during the lecture.

## Final rehearsal list

- [ ] Six demonstrations appear in this order before the summary and closing slides.
- [ ] Every Codex demonstration opens in its own prepared folder.
- [ ] Ollama responds before airplane mode is enabled.
- [ ] The AAP guideline and correction links open in the presentation browser.
- [ ] Every source-dependent prompt names its exact source or exact local file.
- [ ] No real notes, names, screenshots, or EHR tabs are present.
- [ ] The audience sees one verification action after every generated artifact.
