# node-vitest — Bisect Exercise

## Setup

```bash
cd node-vitest
npm install
```

## The Bug

The `capitalize` function is broken — `capitalize("hello")` returns `"hello"` instead of `"Hello"`. It's lowercasing the whole string instead of capitalizing the first letter.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd node-vitest && npx vitest run'
```

## Test Command

```bash
cd node-vitest && npx vitest run
```

A passing run exits 0. A failing run exits non-zero.

## Answer

The first bad commit is `5d1808b` ("Normalize node-vitest capitalize for consistency"), which changed the implementation from `str.charAt(0).toUpperCase() + str.slice(1)` to `str.toLowerCase()`.
