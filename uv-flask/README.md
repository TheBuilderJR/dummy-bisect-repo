# uv-flask — Bisect Exercise

## Setup

```bash
cd uv-flask
uv sync --extra dev
```

## The Bug

The `add` function is returning wrong results. Temperature conversions still work fine.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <first-good-commit>
git bisect run sh -c 'cd uv-flask && uv run pytest tests/'
```

## Test Command

```bash
cd uv-flask && uv run pytest tests/
```

A passing run exits 0. A failing run exits non-zero.

## Notes

Requires Python 3.10+ and uv. Flask is used for the web layer, but the bisect target is the utility functions.
