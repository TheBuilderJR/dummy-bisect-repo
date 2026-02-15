# pip-django — Bisect Exercise

## Setup

```bash
cd pip-django
pip install -r requirements.txt
```

## The Bug

The `word_count` function is returning wrong results — `word_count("hello world")` returns `11` instead of `2`. Other text utilities still work fine.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <scaffold-commit>
git bisect run sh -c 'cd pip-django && pip install -r requirements.txt -q && pytest tests/'
```

## Test Command

```bash
cd pip-django && pytest tests/
```

A passing run exits 0. A failing run exits non-zero.

## Notes

Requires Python 3.10+ and pip. Django is used for the web layer, but the bisect target is the utility functions.

## Answer

The first bad commit is `<TBD>` ("Refine pip-django word_count whitespace handling"), which changed `len(text.split())` to `len(text)`.
