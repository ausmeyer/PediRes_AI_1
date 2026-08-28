# Demonstration 2 prompt

Use only `sources/OpenEvidence_systematic_review_2026.pdf`. Do not browse the web or use facts from model memory.

Create:

- `docs/index.html`: one self-contained, accessible journal-club page with seven full-screen sections navigable by arrow keys. The sections are citation and status; review question; search and inclusion methods; included-study overview; reported strengths; limitations; implications for pediatric residents.
- `README.md`: how to open the page locally and a statement that this is a teaching artifact.
- `SOURCE_LEDGER.md`: each quantitative or evaluative claim, its PDF viewer page, and a short paraphrase of the supporting passage.

Requirements:

- Identify the PDF as an article-in-press accepted manuscript, accepted July 26, 2026.
- Use the exact DOI `10.1038/s41746-026-03077-4`.
- Label findings as findings of the review, not universal facts about all clinical AI.
- Every number must show a PDF viewer page in the HTML and ledger.
- Do not copy or modify figures from the paper.
- Do not invent quotations, citations, PMIDs, or DOIs.
- Do not use external JavaScript, fonts, APIs, or network requests.

After building, verify locally that the HTML opens, contains seven sections, has no external resource URLs, and includes the exact DOI. Report each verification you performed.
