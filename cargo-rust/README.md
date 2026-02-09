# cargo-rust — Bisect Exercise

## Setup

```bash
cd cargo-rust
# No extra setup needed — just needs a Rust toolchain
```

## The Bug

The `reverse_string` function stopped returning the reversed string.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <first-good-commit>
git bisect run sh -c 'cd cargo-rust && cargo test'
```

## Test Command

```bash
cd cargo-rust && cargo test
```

A passing run exits 0. A failing run exits non-zero.
