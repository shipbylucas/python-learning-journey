# Problem Set 5 — CS50P Week 5 (Unit Tests)

In progress: June 4, 2026 (1/4) ⏳

## Problems

- [test_twttr.py](test_twttr/test_twttr.py) — pytest basics, assert statements, function testing — ✅
- [test_bank.py](test_bank/test_bank.py) — testing string logic with multiple cases — ⏳
- [test_plates.py](test_plates/test_plates.py) — testing validation functions — ⏳
- [test_fuel.py](test_fuel/test_fuel.py) — testing fractions and edge cases — ⏳

## Key Learnings

- `pytest` framework: auto-discovers `test_*.py` files
- `assert expected == actual` pattern
- Test files must live in same folder as module being tested
- Organize tests by case: `test_upper()`, `test_lower()`, `test_punctuation()`
- One assertion per concept, not per file