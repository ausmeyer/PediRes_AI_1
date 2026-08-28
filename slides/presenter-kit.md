# Presenter kit — exact run-of-show for six live demonstrations

This is the click-by-click presenter script. The longer source rationale is in [`../briefing/workshops.md`](../briefing/workshops.md), but you should be able to deliver every demonstration from this file alone.

Every vignette and attendance count is synthetic. These demonstrations show possibilities for residents to consider; they are not clinical protocols or tests for the audience.

## The rhythm to use every time

1. Name the practical job in one sentence.
2. Run the supplied prompt without improvising patient facts or sources.
3. Open the resulting file, response, or source where the room can see it.
4. Verify one concrete detail aloud.
5. End with the supplied takeaway and advance.

## Prepare after the repository changes

Run these commands from the repository root:

```bash
cd slides
./render.sh
cd ..
python3 -m pip install -r slides/workshops/requirements.txt
python3 slides/workshops/demo1_fallback.py
ollama pull qwen3.8
./slides/workshops/prepare_demo_folders.sh /tmp/peds-ai-rehearsal
./slides/workshops/prepare_demo_folders.sh /tmp/peds-ai-live-demos
```

Expected results:

- `docs/index.html` is the newly rendered lecture.
- Demonstration 1 backup files are in `slides/workshops/demo1_out/`.
- Ollama reports that `qwen3.8` is available locally.
- `/tmp/peds-ai-rehearsal/` and `/tmp/peds-ai-live-demos/` each contain folders `01` through `06`.

The folder-preparation script will not overwrite a prior folder. If either destination already exists, choose a new explicit path and use that same path throughout the rehearsal or lecture.

## Complete one rehearsal

1. Use `/tmp/peds-ai-rehearsal/`, not the live folder.
2. Perform Demonstrations 1–6 below in order.
3. Leave the completed rehearsal outputs available as a visual backup.
4. Confirm that the local model answers while Wi-Fi is off.
5. Confirm that the official AAP guideline and correction pages open while Wi-Fi is on:
   - guideline DOI: `10.1542/peds.2021-052228`
   - correction DOI: `10.1542/peds.2021-054063`
6. Open the Artsi PDF and confirm that PDF viewer page 3 contains the abstract sentence reporting 11 included studies.
7. Open the FDA PDF and confirm that PDF viewer page 2 identifies it as a discussion document rather than guidance.
8. Close or hide every window containing email, messaging, an EHR, a real patient name, or unrelated browser history.

## Set the room 20 minutes before the lecture

1. Connect the projector and select the intended audio/video output.
2. Open `docs/index.html` in the presentation browser.
3. Enter presentation mode and confirm that speaker notes are visible only on the presenter display.
4. Return to the title slide.
5. Open Codex at `/tmp/peds-ai-live-demos/`.
6. Open one terminal at the same folder.
7. Open the system Wi-Fi control so airplane-mode status can be shown during Demonstration 3.
8. Open the official AAP guideline and correction in two browser tabs, then leave those tabs untouched for Demonstration 4.
9. Open a file browser at `/tmp/peds-ai-live-demos/` so generated files are easy to reach.
10. Keep the completed `/tmp/peds-ai-rehearsal/` outputs available but off screen.
11. Confirm the projected screen contains only invented teaching material.
12. Keep Wi-Fi on until Demonstration 3.

## Demonstration 1 — Codex makes office files

**Working folder:** `/tmp/peds-ai-live-demos/01-office-files/`

**Supplied inputs:** `STEM.md`, `PROMPT.md`

**Expected outputs:** `family_update.docx`, `oxygen_wean_tracker.xlsx`, `noon_conference.pptx`

### Presenter steps

1. Advance to **“Demonstration 1 — files, not paragraphs.”**
2. Say: “The job is to turn one synthetic stem into three files that people can inspect.”
3. Point once to `SYNTHETIC TEACHING CASE — NOT A REAL PATIENT` in the supplied stem.
4. In Codex, open `/tmp/peds-ai-live-demos/01-office-files/` as the working folder.
5. Start a fresh task in that folder.
6. Open `PROMPT.md`, copy its entire contents, paste them into Codex, and submit once.
7. If Codex asks to create or inspect the three named files in this folder, allow those in-scope actions.
8. Wait until Codex reports that all three files exist and have been inspected.
9. Open `family_update.docx`.
10. Scroll to the final line and point to the exact sentence `This is a teaching example.`
11. Open `oxygen_wean_tracker.xlsx`.
12. Count the six data rows below the header.
13. Point across the headers and confirm that there is no medication column.
14. Select one cell in `hours since the last wean attempt` and show that it contains a formula rather than a typed narrative value.
15. Open `noon_conference.pptx` in slide-sorter or thumbnail view.
16. Confirm that there are eight slides.
17. Open a slide that needs a citation and point to `PLACEHOLDER—VERIFY BEFORE TEACHING` rather than an invented identifier.
18. Say: “Codex can create usable drafts, but we still open the files and inspect the constraints.”
19. Return to the lecture and advance.

### Expected result

- One Word file ends with the exact teaching label.
- One spreadsheet has six synthetic rows, the requested formula, and no medication column.
- One eight-slide deck marks unverified citations as placeholders.

### If the live build is still running

1. Say: “The same prompt has a deterministic local backup, so I’ll keep us moving.”
2. Open `slides/workshops/demo1_out/`.
3. Continue with Steps 9–19 using those three files.

## Demonstration 2 — Codex builds a journal-club page

**Working folder:** `/tmp/peds-ai-live-demos/02-journal-club/`

**Only allowed source:** `sources/OpenEvidence_systematic_review_2026.pdf`

**Expected outputs:** `docs/index.html`, `README.md`, `SOURCE_LEDGER.md`

### Presenter steps

1. Advance to **“Demonstration 2 — one PDF becomes a journal-club page.”**
2. Say: “The job is to turn one named paper into a page whose claims can be traced back to that paper.”
3. In Codex, open `/tmp/peds-ai-live-demos/02-journal-club/`.
4. Start a fresh task and ensure web access is off for this task.
5. Open `PROMPT.md`, copy all of it, paste it into Codex, and submit once.
6. If Codex asks to read the local PDF or create files under this folder, allow those in-scope actions.
7. Wait until Codex reports that `docs/index.html`, `README.md`, and `SOURCE_LEDGER.md` exist.
8. Open `docs/index.html` locally in the browser.
9. Press the right-arrow key six times, pausing briefly at each section, to show all seven sections.
10. Confirm that the page identifies the source as an article-in-press accepted manuscript and shows DOI `10.1038/s41746-026-03077-4`.
11. Open `SOURCE_LEDGER.md`.
12. Find the row for the claim that the review included 11 studies.
13. Note the cited PDF viewer page.
14. Open `sources/OpenEvidence_systematic_review_2026.pdf` in the PDF viewer.
15. Go to PDF viewer page 3.
16. Point to the abstract sentence that reports 11 included studies.
17. Say: “The useful chain is named source, generated artifact, then page-level verification.”
18. Return to the lecture and advance.

### Expected result

- The page has seven keyboard-navigable sections and no external resources.
- The DOI and manuscript status are exact.
- The ledger connects the “11 studies” claim to the source; PDF viewer page 3 confirms it.

## Demonstration 3 — Ollama works offline

**Working folder:** `/tmp/peds-ai-live-demos/03-offline-ollama/`

**Supplied input:** `demo3_ollama_prompt.txt`

### Presenter steps

1. Advance to **“Demonstration 3 — local model, airplane mode.”**
2. Say: “The job is to summarize one supplied synthetic note without sending the prompt to a hosted model.”
3. Open the Wi-Fi control where the room can see it.
4. Turn Wi-Fi off.
5. In the terminal, run exactly:

   ```bash
   cd /tmp/peds-ai-live-demos/03-offline-ollama
   ollama run qwen3.8 < demo3_ollama_prompt.txt
   ```

6. Wait for the response to finish.
7. Show the four requested sections: one-sentence summary, problem list, overnight contingencies for clinician review, and three family questions.
8. Search or scan for `MISSING`.
9. Point out that the supplied note has no current weight and no numeric urine output.
10. Confirm that the response does not invent either value. If it phrases an omission without the required word `MISSING`, say that it did not follow the stated constraint.
11. Say: “Local execution controls where the prompt goes; it does not certify that the summary is correct or hospital-approved.”
12. Turn Wi-Fi back on before leaving this demonstration.
13. Confirm that the Wi-Fi indicator shows a connection.
14. Return to the lecture and advance.

### Expected result

- Ollama completes while Wi-Fi is visibly off.
- The response contains exactly four sections.
- Absent facts are marked `MISSING` rather than supplied from inference.

### If `qwen3.8` does not start

Use only the already-downloaded, already-rehearsed 8B-class Ollama model chosen before the lecture. Change the model name in the command, keep the same prompt, and do not begin a download on stage.

## Demonstration 4 — one question, three source conditions

**Parent folder:** `/tmp/peds-ai-live-demos/04-source-conditions/`

**Synthetic case:** a well-appearing 26-day-old with fever; urinalysis and inflammatory markers are deliberately absent

### Presenter steps

1. Advance to **“Demonstration 4 — one question, three source conditions.”**
2. Confirm that Wi-Fi is back on.
3. Say: “The job is to ask the same question three times while changing only the allowed source material.”
4. Point to the five comparison items on the slide: source named, age-specific, missing data requested, correction reviewed, and no made-up quotation.

#### Condition A — case only

5. Open `/tmp/peds-ai-live-demos/04-source-conditions/A-no-source/` in Codex.
6. Start a fresh task and keep web access off.
7. Paste the entire `PROMPT.md` and submit once.
8. When the response appears, identify the five labeled parts.
9. Point out whether it directly says that it cannot quote the AAP guideline from the allowed material.
10. Confirm that it requests the missing urinalysis and inflammatory markers.

#### Condition B — guideline allowed

11. Open `/tmp/peds-ai-live-demos/04-source-conditions/B-guideline/` in Codex.
12. Start a new task so Condition A is not in the conversation.
13. Turn web access on for this task.
14. Paste the entire `PROMPT.md` and submit once.
15. Permit access only to the official AAP article listed in `SOURCES.md`.
16. When the response appears, point to the 22–28-day age group, the exact source used, and the still-missing urinalysis and inflammatory markers.
17. If the official article cannot be opened, show the bounded “cannot open” response; do not let Codex reconstruct the wording from memory.

#### Condition C — guideline and correction allowed

18. Open `/tmp/peds-ai-live-demos/04-source-conditions/C-guideline-and-correction/` in Codex.
19. Start another new task.
20. Keep web access on.
21. Paste the entire `PROMPT.md` and submit once.
22. Permit access only to the official guideline and correction listed in `SOURCES.md`.
23. When the response appears, point to the guideline location, the correction source, and the explicit statement about whether the correction changes the relevant conclusion.
24. Compare A, B, and C using the five items on the slide.
25. Say: “Retrieval is a source choice. A defined source set makes the answer more traceable and makes missing inputs easier to see.”
26. Return to the lecture and advance.

### Expected contrast

- A stays cautious and does not fabricate guideline wording.
- B grounds the answer in the official guideline and identifies the relevant age group.
- C checks both the guideline and its correction rather than assuming the first document is the whole record.
- All three preserve the missing case data instead of silently filling it in.

## Demonstration 5 — Codex repairs and tests a page

**Working folder:** `/tmp/peds-ai-live-demos/05-repair-page/`

**Supplied inputs:** `broken_attendance.html`, `PROMPT.md`

### Presenter steps

1. Advance to **“Demonstration 5 — Codex repairs the artifact.”**
2. Say: “The job is to repair an interaction in an existing file and test the result.”
3. Open `broken_attendance.html` in a browser before using Codex.
4. Enter `4` in the week field and submit.
5. Show that the Week 4 bar does not become orange and call this the interaction issue.
6. Open `/tmp/peds-ai-live-demos/05-repair-page/` in Codex.
7. Start a fresh task.
8. Open `PROMPT.md`, copy all of it, paste it into Codex, and submit once.
9. Allow Codex to inspect and edit only the existing HTML file.
10. Wait for Codex to report the cause, the edit, and the five requested test results.
11. Reload `broken_attendance.html` in the browser so the edited file is active.
12. Enter `4`: confirm that exactly Week 4 turns orange and the page reports `25`.
13. Enter `1`: confirm that exactly Week 1 turns orange and the page reports `19`.
14. Enter `8`: confirm that exactly Week 8 turns orange and the page reports `24`.
15. Enter `9`: confirm that no bar is orange and the page displays `Enter a week from 1 to 8.`
16. Clear the field and submit a blank value: confirm the same message and no orange bar.
17. Point out that the eight displayed counts remain `19, 22, 17, 25, 23, 20, 26, 24`.
18. Say: “For an artifact, the useful loop is open, inspect, edit, run, and verify.”
19. Return to the lecture and advance.

### Expected result

- The existing file is repaired in place without a framework or network dependency.
- Valid inputs highlight exactly one matching bar and report its unchanged count.
- Invalid or blank inputs highlight no bar and show the exact range message.
- The accessible label and live status remain present.

## Demonstration 6 — Codex builds a bounded evidence brief

**Working folder:** `/tmp/peds-ai-live-demos/06-source-packet/`

**Allowed packet:** `SOURCE_PACKET.md` plus the three PDFs in `sources/`

**Expected output:** `evidence_brief.md`

### Presenter steps

1. Advance to **“Demonstration 6 — a fixed packet, a bounded brief.”**
2. Say: “The job is to synthesize a fixed packet and make the boundary of that packet visible.”
3. Open `/tmp/peds-ai-live-demos/06-source-packet/` in Codex.
4. Start a fresh task and turn web access off for that task.
5. Open `PROMPT.md`, copy all of it, paste it into Codex, and submit once.
6. Allow Codex to read `SOURCE_PACKET.md` and the three local PDFs and to create `evidence_brief.md`.
7. Wait until Codex reports that it checked all five cited viewer pages.
8. Open `evidence_brief.md`.
9. Point to the two-sentence bounded answer and the table with exactly five claim rows.
10. Point to the document-type section and confirm that it calls Artsi et al. a systematic review and the WHO and FDA documents discussion papers, not guidelines.
11. Open `sources/FDA_GenAI_medical_devices_discussion_2026.pdf`.
12. Go to PDF viewer page 2.
13. Point to the statement that the paper is for discussion purposes and is not draft or final guidance; compare it with the corresponding row in `evidence_brief.md`.
14. Return to `evidence_brief.md`.
15. Find the sentinel question: `Which document reports a pediatric randomized trial of AI-assisted lumbar-puncture decisions?`
16. Confirm that the answer begins with the exact words `NOT IN PACKET`.
17. Say: “A bounded packet can make synthesis inspectable. It cannot make absent pediatric evidence appear.”
18. Return to the lecture and advance.

### Expected result

- The brief contains exactly five page-cited claims.
- It distinguishes a systematic review from two discussion papers.
- The FDA claim traces to PDF viewer page 2.
- The off-packet sentinel begins `NOT IN PACKET`.

## Close the lecture

1. On **“Six habits to remember,”** point through the six habits once without reopening any demonstration.
2. On **“Three questions before you copy,”** read the three questions as a reusable pause before someone uses generated material.
3. Advance to **“The End / Q&A.”**
4. Leave the backup slides after the closing slide unless a question makes one useful.

## Keep the lecture moving

- **A Codex task is slow:** open the matching completed output from `/tmp/peds-ai-rehearsal/`, perform the same visible verification, and continue.
- **The network becomes unavailable:** Demonstrations 1, 2, 3, 5, and 6 are local. For Demonstration 4, use the official AAP tabs opened before the lecture; if they are unavailable, show the prepared prompts and explain what each source condition permits without substituting an unofficial mirror.
- **The Ollama model is unavailable:** use only the already-tested local substitute chosen during rehearsal. Do not download a model on stage.
- **A generated claim has no traceable page:** say, “This claim is not ready to reuse because I cannot trace it,” remove it from consideration, and continue with a verifiable row.
- **A generated file does not open:** use the completed rehearsal artifact and perform the same inspection steps.

## Final presenter check

- [ ] All six demonstrations appear in order before the summary and closing slides.
- [ ] Every Codex demonstration begins in a fresh task and the stated folder.
- [ ] Web access is off for Demonstrations 2 and 6, off for Condition A, and on for Conditions B and C.
- [ ] Wi-Fi is visibly off only for Demonstration 3 and is restored before Demonstration 4.
- [ ] The official AAP guideline and correction tabs are already open.
- [ ] The Artsi PDF opens to viewer page 3 and the FDA PDF opens to viewer page 2.
- [ ] The audience sees at least one file, source, formula, or acceptance test after every generated result.
- [ ] No real patient note, name, EHR, email, or message is visible.

## Theme and deployment

Source: `slides/lecture.qmd`

Styles: `slides/mclane.scss`

Rendered GitHub Pages entry point: `docs/index.html`
