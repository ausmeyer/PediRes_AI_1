# Live demonstration files

The complete presenter runbook is [`../../briefing/workshops.md`](../../briefing/workshops.md). All clinical cases and attendance counts here are invented.

Run this once before rehearsal or the lecture:

```bash
./prepare_demo_folders.sh /tmp/peds-ai-live-demos
```

The preparation script creates six isolated folders and copies the exact prompt, case, web page, and PDF inputs into each. It refuses to overwrite an existing destination.

| File | Demonstration | Purpose |
|---|---:|---|
| [`STEM.md`](STEM.md), [`demo1_prompt.md`](demo1_prompt.md) | 1 | Synthetic bronchiolitis stem and exact Codex file-building prompt |
| [`lab1_fallback.py`](lab1_fallback.py) | 1 | Prebuilt Word, Excel, and PowerPoint fallback |
| [`demo2_prompt.md`](demo2_prompt.md) | 2 | Exact Codex prompt for the named Artsi et al. PDF |
| [`demo3_ollama_prompt.txt`](demo3_ollama_prompt.txt) | 3 | Complete offline Ollama prompt and synthetic H&P |
| `demo4_*` | 4 | One exact case, canonical AAP links, and three source-condition prompts |
| [`broken_attendance.html`](broken_attendance.html), [`demo5_prompt.md`](demo5_prompt.md) | 5 | Intentionally broken page and explicit Codex acceptance tests |
| [`SOURCE_PACKET.md`](SOURCE_PACKET.md), [`demo6_prompt.md`](demo6_prompt.md) | 6 | Three-PDF manifest and exact source-bounded synthesis prompt |

`KEY.md` and `lab2_fallback.py` are retained as legacy files but are no longer part of the lecture.
