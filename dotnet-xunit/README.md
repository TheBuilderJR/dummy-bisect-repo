# dotnet-xunit — Bisect Exercise

## Setup

```bash
cd dotnet-xunit
dotnet restore
```

## The Bug

The `Repeat` function is broken — `Repeat("abc", 3)` returns `"abc"` instead of `"abcabcabc"`. It's only repeating once regardless of the count.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <good-commit>
git bisect run sh -c 'cd dotnet-xunit && dotnet test --no-restore'
```

## Test Command

```bash
cd dotnet-xunit && dotnet test
```

A passing run exits 0. A failing run exits non-zero.

## Answer

The first bad commit is `<bad-commit>` ("Streamline dotnet-xunit Repeat loop logic"), which changed `i < count` to `i < 1` in the loop condition.
