# Teaching key — fictional drug only

- Drug name: `teachicillin` (fictional; do not substitute a real formulary drug)
- Route: oral
- Dose: 10 mg per kg per dose
- Frequency: every 8 hours
- Maximum: 400 mg per dose
- If `weight_kg` is under 2: do not compute a dose; write `TOO_SMALL` in the dose cell
- Spreadsheet inputs: `weight_kg`, `age_months`
- The dose formula must cap: `MIN(weight_kg*10, 400)`
- `age_months` is recorded only; it does not change the dose in this key
