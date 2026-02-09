# go-test — Bisect Exercise

## Setup

```bash
cd go-test
# No extra setup needed — just needs a Go toolchain
```

## The Bug

The `Divide` function is returning incorrect results — `Divide(10, 2)` returns `20` instead of `5`. It's multiplying instead of dividing.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd go-test && go test ./...'
```

## Test Command

```bash
cd go-test && go test ./...
```

A passing run exits 0. A failing run exits non-zero.

## Notes

This project uses the standard Go testing framework — no third-party dependencies required.

## Answer

The first bad commit is `16a6d6d` ("Optimize go-test Divide for performance"), which changed `return a / b, nil` to `return a * b, nil`.
