# cargo-rust — Bisect Exercise

## Setup

```bash
cd cargo-rust
# No extra setup needed — just needs a Rust toolchain
```

## The Bug

The `reverse_string` function stopped reversing — `reverse_string("hello")` returns `"hello"` instead of `"olleh"`.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd cargo-rust && cargo test'
```

## Test Command

```bash
cd cargo-rust && cargo test
```

A passing run exits 0. A failing run exits non-zero.

## Answer

The first bad commit is `e1dd2bf` ("Simplify cargo-rust reverse_string implementation"), which changed `s.chars().rev().collect()` to `s.to_string()`.
