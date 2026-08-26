# Labs 1 and 2, on your laptop

Synthetic only. Not a real child. Not a formulary. Longer recipes: [`../../briefing/workshops.md`](../../briefing/workshops.md).

| File | Lab | What it is |
|---|---|---|
| [`STEM.md`](STEM.md) | 1 | Bronchiolitis stem we wrote (not model output) |
| [`lab1_fallback.py`](lab1_fallback.py) | 1 | Writes Word, Excel, and PowerPoint into `lab1_out/` |
| [`KEY.md`](KEY.md) | 2 | Fictional `teachicillin` rules we wrote |
| [`lab2_fallback.py`](lab2_fallback.py) | 2 | Writes `lab2_out/dosing.xlsx` — missing the 400 mg cap on purpose |
| [`requirements.txt`](requirements.txt) | — | `python-docx`, `openpyxl`, `python-pptx` |

```bash
pip install -r requirements.txt
python lab1_fallback.py
python lab2_fallback.py
```

You can also paste `STEM.md` into ChatGPT with no identifiers, ask for a Python script, and run that script locally.
