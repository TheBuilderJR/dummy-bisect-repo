# node-vitest — Bisect Exercise

## Setup

```bash
cd node-vitest
npm install
```

## The Bug

The `capitalize` function is broken — it's lowercasing instead of capitalizing.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <first-good-commit>
git bisect run sh -c 'cd node-vitest && npx vitest run'
```

## Test Command

```bash
cd node-vitest && npx vitest run
```

A passing run exits 0. A failing run exits non-zero.
