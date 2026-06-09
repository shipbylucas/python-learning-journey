# **Problem Set 6 — CS50P Week 6 (File I/O)**

Completed: June 9, 2026 (4/4) ✅

## **Problems**

- [lines.py](vscode-file://vscode-app/Volumes/Cursor%20Installer/Cursor.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/lines.py) — count lines of code, skip comments and blanks, `sys.argv` — ✅
- [pizza.py](vscode-file://vscode-app/Volumes/Cursor%20Installer/Cursor.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/pizza.py) — read CSV, format as table with `tabulate` — ✅
- [scourgify.py](vscode-file://vscode-app/Volumes/Cursor%20Installer/Cursor.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/scourgify.py) — read/write CSV, `csv.DictReader`/`DictWriter` — ✅
- [shirt.py](vscode-file://vscode-app/Volumes/Cursor%20Installer/Cursor.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/shirt.py) — image manipulation with `PIL`, resize and overlay — ✅

## **Key Learnings**

- File I/O with `open()`, `with` statement for auto-close
- Command-line arguments via `sys.argv`
- `sys.exit("message")` for graceful errors
- Reading file line by line vs `.readlines()`
- Stripping whitespace with `.strip()` before parsing
- CSV parsing with `csv.reader` (list) vs `csv.DictReader` (dict)
- Writing CSV with headers using `csv.DictWriter` + `writeheader()`
- Formatting tables with `tabulate` library
- Image handling with `PIL`: `Image.open()`, `.resize()`, `.paste()` for overlay
- Matching file extensions between input and output files
- `FileNotFoundError` / `OSError` handling for invalid image paths

