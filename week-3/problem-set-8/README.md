# **Problem Set 8 — CS50P Week 8 (Object-Oriented Programming)**

In progress: June 15, 2026 (2/3) 🟡

## **Problems**

- [seasons.py](seasons.py) — calculate age in minutes from birthdate, `date.today()`, `inflect` for number-to-words — ✅
- [jar.py](jar.py) — Cookie Jar class, `@property`/`@setter` with validation, `deposit`/`withdraw`, `__str__` for 🍪 output — ✅
- shirt.py — CS50 Shirt, OOP refactor — ⏳

## **Key Learnings**

- Defining classes with `class` and the `__init__` constructor
- Instance attributes vs class attributes
- `self` and how methods reference the instance
- `@property` decorator for getters
- `@setter` for controlled attribute assignment with validation
- Raising `ValueError` inside setters to enforce constraints
- `__str__` for readable object representation (string multiplication for 🍪)
- Guarding state changes — `deposit`/`withdraw` checking against capacity
- `date.today()` and date arithmetic with `datetime`
- `inflect` library for natural-language number formatting