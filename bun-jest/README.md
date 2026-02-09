# bun-jest — Bisect Exercise

## Setup

```bash
cd bun-jest
bun install
```

## The Bug

The `multiply` function is returning incorrect results. It used to work.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <first-good-commit>
git bisect run sh -c 'cd bun-jest && bun test'
```

## Test Command

```bash
cd bun-jest && bun test
```

A passing run exits 0. A failing run exits non-zero.
