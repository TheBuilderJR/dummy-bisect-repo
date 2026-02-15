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
git bisect good c348aaf
git bisect run sh -c 'cd dotnet-xunit && dotnet test --no-restore'
```

## Test Command

```bash
cd dotnet-xunit && dotnet test
```

A passing run exits 0. A failing run exits non-zero.

## Notes

Requires .NET 8.0 SDK. Uses xUnit as the test framework with the standard `dotnet test` runner.

## Answer

The first bad commit is `349caf0` ("Streamline dotnet-xunit Repeat loop logic"), which changed `i < count` to `i < 1` in the loop condition.
