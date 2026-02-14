# python-cpp — Bisect Exercise

## Setup

```bash
cd python-cpp
python setup.py develop
```

This compiles the C++ extension and installs the package in development mode.

## The Bug

The `dot_product` function returns incorrect results — `dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0])` returns `15.0` instead of `32.0`.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good 039259b
git bisect run sh -c 'cd python-cpp && python setup.py develop 2>&1 && python -m pytest tests/'
```

## Test Command

```bash
cd python-cpp && python setup.py develop && python -m pytest tests/
```

A passing run exits 0. A failing run exits non-zero.

## Answer

> **Spoiler below** — try to find it yourself first!

The first bad commit is the one titled "Optimize python-cpp dot_product accumulation", which changed `result += a * b` to `result += a + b` in the C++ source.

## Notes

- Requires a C++ compiler (`g++`) and Python development headers (`python3-dev`)
- The `setup.py develop` step is required before running tests — it compiles the C++ extension in-place
- Unlike the other exercises, this one has a build step that must run during bisect
