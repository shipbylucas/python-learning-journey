# Problem Set 6 — CS50P Week 6 (File I/O)

In progress: June 6, 2026 (1/4) ⏳

## Problems

- [lines.py](lines/lines.py) — count lines of code, skip comments and blanks, `sys.argv` — ✅
- [pizza.py](pizza/pizza.py) — read CSV, format as table with `tabulate` — ⏳
- [scourgify.py](scourgify/scourgify.py) — read/write CSV, `csv.DictReader`/`DictWriter` — ⏳
- [shirt.py](shirt/shirt.py) — image manipulation with `PIL`, resize and overlay — ⏳

## Key Learnings

- File I/O with `open()`, `with` statement for auto-close
- Command-line arguments via `sys.argv`
- `sys.exit("message")` for graceful errors
- Reading file line by line vs `.readlines()`
- Stripping whitespace with `.strip()` before parsing