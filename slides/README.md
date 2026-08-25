# Slide platform for the McLane hour

**Author in Quarto Reveal.js. Carry a frozen PDF (and a PowerPoint export) as fail-safes. Do not make PowerPoint the source of truth.**

This is a decision note, not the deck. No slides have been drafted yet.

## Recommendation, in one line

| Role | Format |
|---|---|
| Source of truth (git) | `slides/lecture.qmd` → Reveal.js HTML |
| Share with residents after | GitHub Pages URL + PDF |
| Podium fail-safe | PDF on the laptop, then `.pptx` if the room PC only runs PowerPoint |
| GME archive, if they demand Office | the exported `.pptx`, not a separately maintained deck |

PowerPoint is the **export**, not the authoring environment. Excel is the wrong medium for a lecture (already settled).

## Why this mix, for this talk

**Quarto (or Markdown Reveal) matches the teaching point.** Workshop 2 is “Markdown → JavaScript slides on GitHub Pages, no coding by the resident.” If the hour itself is a Reveal deck, the workshop is not a detour. Residents can reopen the same URL on a phone in the back row.

**The papers now live in this repo.** Quarto can cite `briefing/papers/` the same way the briefing cites them. A `.pptx` you click around in on a plane will drift from the ledger.

**Hospital projector reality is unforgiving.** Assume: HDMI, a locked-down Windows box, flaky Wi-Fi, and a clicker that only feels native in PowerPoint. Reveal in Chrome fullscreen works when you control the laptop. PDF always works. Native PowerPoint is the format a co-presenter can advance if they take over.

**You will edit 10 minutes before noon conference.** That is the one real argument *for* PowerPoint. Solve it by freezing exports the night before (`lecture.pdf`, `lecture.pptx`) rather than by making `.pptx` the master. If you must tweak at the podium, tweak the PDF/PPTX and patch git later.

## When PowerPoint should win instead

Use PowerPoint as the master only if one of these is true:

- A co-presenter will own the deck and only uses Office.
- GME/CME requires a native `.pptx` with their template and you cannot export into it cleanly.
- The podium PC has no browser you can trust and you will not be allowed to plug in your own laptop.

If that is the world, still keep a Markdown outline in git so Workshop 2 has a source file to show.

## What “something else” is worth considering

| Tool | Use it? | Why |
|---|---|---|
| **Quarto Reveal.js** | **Yes (default)** | One toolchain for lecture + PDF + optional PPTX; citations; GitHub Pages |
| **Marp** or **reveal-md** | Yes, if you do not want Quarto installed | Same pedagogy, less machinery |
| **Raw Reveal.js HTML** | Yes for Workshop 2 | That *is* the resident-replicable path |
| **PowerPoint** | Export / fail-safe, or master only in the cases above | Hospital-native; version-control hostile |
| **Google Slides** | No as master | Hospital accounts often block; citations and git are worse |
| **Keynote** | No | Podium is likely Windows |
| **Beamer** | No | Wrong aesthetic for this audience |
| **Gamma / Tome / Beautiful.ai** | No | Opaque generation; you cannot audit claims the way the briefing requires |

## Practical build (when we make the deck)

1. One `slides/lecture.qmd` following the live spine in the briefing (about 25–35 slides, not 40 pages dumped into 60 slides).
2. `quarto render slides/lecture.qmd` → HTML for GitHub Pages.
3. Same render, or a print CSS / `decktape`, → `lecture.pdf`.
4. `quarto render slides/lecture.qmd --to pptx` (or Pandoc) → `lecture.pptx` for the GME dropbox and the room PC.
5. Night-before freeze of PDF + PPTX on the presenter laptop **and** a USB stick.

Do not animate heavily. The hour is talking + two live workshops. Slides are a spine, not a script.

## What this is not

This file does not choose fonts, a BSWH template, or a slide count. Those wait until the deck is actually built.
