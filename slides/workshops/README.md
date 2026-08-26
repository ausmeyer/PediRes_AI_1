# Lab fallbacks

Synthetic only. Full recipes: [`../../briefing/workshops.md`](../../briefing/workshops.md).

| File | Lab | What it is |
|---|---|---|
| [`lab1_fallback.py`](lab1_fallback.py) | 1 (live) | Writes Word, Excel, and PowerPoint into `lab1_out/` |
| [`lab2_fallback.py`](lab2_fallback.py) | 2 (live) | Writes `lab2_out/dosing.xlsx` — missing the 400 mg cap on purpose |
| [`STEM.md`](STEM.md) | 1 | Human-written bronchiolitis stem. Not model output. Not a real child. |
| [`KEY.md`](KEY.md) | 2 | Fictional `teachicillin` key |
| [`requirements.txt`](requirements.txt) | — | `python-docx`, `openpyxl`, `python-pptx` |

From this folder:

```bash
pip install -r requirements.txt
python lab1_fallback.py
python lab2_fallback.py
```
