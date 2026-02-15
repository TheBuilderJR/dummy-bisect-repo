# deno-nextjs — Bisect Exercise

## Setup

```bash
cd deno-nextjs
# No extra setup needed — just needs a Deno runtime
```

## The Bug

The `chunk` function is broken — `chunk([1, 2, 3, 4, 5], 2)` returns `[[1],[2],[3],[4],[5]]` instead of `[[1,2],[3,4],[5]]`. It's ignoring the chunk size and producing single-element arrays.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <good-commit>
git bisect run sh -c 'cd deno-nextjs && deno test'
```

## Test Command

```bash
cd deno-nextjs && deno test
```

A passing run exits 0. A failing run exits non-zero.

## Answer

The first bad commit is `<bad-commit>` ("Optimize deno-nextjs chunk iteration step"), which changed `i += size` and `arr.slice(i, i + size)` to `i += 1` and `arr.slice(i, i + 1)`.
