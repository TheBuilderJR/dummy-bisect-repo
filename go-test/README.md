# go-test — Bisect Exercise

## Setup

```bash
cd go-test
# No extra setup needed — just needs a Go toolchain
```

## The Bug

The `Divide` function is returning incorrect results (not dividing properly).

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <first-good-commit>
git bisect run sh -c 'cd go-test && go test ./...'
```

## Test Command

```bash
cd go-test && go test ./...
```

A passing run exits 0. A failing run exits non-zero.
