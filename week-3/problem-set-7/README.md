# **Problem Set 7 — CS50P Week 7 (Regular Expressions)**

Completed: June 11, 2026 (5/5) ✅

## **Problems**

- [numb3rs.py](numb3rs.py) — validate IPv4 address, `re.search` with capture groups and range check — ✅
- [watch.py](watch.py) — extract YouTube embed URL, `re.search` + `.group()` — ✅
- [working.py](working.py) — convert "9 AM to 5 PM" to 24-hour format, `re.fullmatch` + time validation — ✅
- [um.py](um.py) — count standalone "um" occurrences, `re.findall` with word boundaries — ✅
- [response.py](response.py) — validate email format with `validators` / regex — ✅

## **Key Learnings**

- `re.search` (anywhere) vs `re.match` (start) vs `re.fullmatch` (entire string)
- Capture groups `()` and back-referencing with `.group(n)`
- Character classes `[a-z]`, `\d`, `\w`, `\s` and their negations
- Anchors `^` (start) and `$` (end) for full-string validation
- Word boundaries `\b` to match standalone words (e.g. "um" not "yummy")
- Quantifiers: `*`, `+`, `?`, `{n}`, `{n,m}`
- Non-greedy matching with `*?` / `+?`
- `re.IGNORECASE` flag for case-insensitive matching
- `re.sub()` for find-and-replace
- Raw strings `r"..."` to avoid escaping backslashes
- Validating ranges that regex alone can't enforce (e.g. IP octets 0–255)