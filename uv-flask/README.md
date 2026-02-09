# uv-flask — Bisect Exercise

## Setup

```bash
cd uv-flask
uv sync --extra dev
```

## The Bug

The `add` function is returning wrong results — `add(2, 3)` returns `-1` instead of `5`. Temperature conversions still work fine.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd uv-flask && uv run pytest tests/'
```

## Test Command

```bash
cd uv-flask && uv run pytest tests/
```

A passing run exits 0. A failing run exits non-zero.

## Notes

Requires Python 3.10+ and uv. Flask is used for the web layer, but the bisect target is the utility functions.

## Answer

The first bad commit is `e58d699` ("Refactor uv-flask arithmetic helpers"), which changed `return a + b` to `return a - b`.
