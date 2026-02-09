# bun-jest — Bisect Exercise

## Setup

```bash
cd bun-jest
bun install
```

## The Bug

The `multiply` function is returning incorrect results — `multiply(3, 4)` returns `13` instead of `12`.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd bun-jest && bun test'
```

## Test Command

```bash
cd bun-jest && bun test
```

A passing run exits 0. A failing run exits non-zero.

## Answer

The first bad commit is `ecbff1e` ("Update bun-jest multiply with rounding adjustment"), which changed `return a * b` to `return a * b + 1`.
