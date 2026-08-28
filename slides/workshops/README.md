# Workshop fallback files

Invented bronchiolitis stem and a fictional dosing key. Longer recipes: [`../../briefing/workshops.md`](../../briefing/workshops.md).

| File | Workshop | What it is |
|---|---|---|
| [`STEM.md`](STEM.md) | 1 | Bronchiolitis stem we wrote (not model output) |
| [`lab1_fallback.py`](lab1_fallback.py) | 1 | Writes Word, Excel, and PowerPoint into `lab1_out/` |
| [`KEY.md`](KEY.md) | 6 | Fictional `teachicillin` rules we wrote |
| [`lab2_fallback.py`](lab2_fallback.py) | 6 | Legacy filename; writes `lab2_out/dosing.xlsx` with the 400 mg cap missing on purpose |
| [`requirements.txt`](requirements.txt) | — | `python-docx`, `openpyxl`, `python-pptx` |

```bash
pip install -r requirements.txt
python lab1_fallback.py
python lab2_fallback.py
```

You can also paste `STEM.md` into ChatGPT with no identifiers, ask for a Python script, and run that script locally.
