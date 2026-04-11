# Git Bisect Practice Repo

Small, intentionally broken projects for learning and practicing `git bisect`.

Each exercise gives you:

- a known-good commit to mark with `git bisect good`
- a deterministic command you can use with `git bisect run`
- one regression introduced somewhere later in history

The root README stays mostly spoiler-light. If you want setup details or the answer for a specific exercise, open that exercise's `README.md`. The only exception is `script.sh`, which lives at the repository root.

## Quick Start

1. Pick an exercise from the catalog below.
2. Run any one-time setup noted in that exercise README.
3. From the repository root, start bisecting:

```bash
git bisect start
git bisect bad HEAD
git bisect good <known-good-commit>
git bisect run sh -c '<command>'
git bisect reset
```

Example using `go-test`:

```bash
git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd go-test && go test ./...'
git bisect reset
```

## Exercise Catalog

| Exercise | Stack | What is broken at `HEAD` | Known-good commit | Command for `git bisect run` |
| --- | --- | --- | --- | --- |
| `script.sh` | Bash | exits `1` instead of `0` | `db09c77` | `./script.sh` |
| [bun-jest](bun-jest/README.md) | Bun + Jest | `multiply(3, 4)` returns the wrong value | `c8a9b34` | `cd bun-jest && bun test` |
| [uv-flask](uv-flask/README.md) | uv + Flask + pytest | `add(2, 3)` returns `-1` instead of `5` | `c8a9b34` | `cd uv-flask && uv run pytest tests/` |
| [node-vitest](node-vitest/README.md) | Node + Vitest | `capitalize("hello")` returns `"hello"` instead of `"Hello"` | `c8a9b34` | `cd node-vitest && npx vitest run` |
| [cargo-rust](cargo-rust/README.md) | Rust + cargo test | `reverse_string("hello")` returns `"hello"` instead of `"olleh"` | `c8a9b34` | `cd cargo-rust && cargo test` |
| [go-test](go-test/README.md) | Go + go test | `Divide(10, 2)` returns `20` instead of `5` | `c8a9b34` | `cd go-test && go test ./...` |
| [python-cpp](python-cpp/README.md) | Python + C++ extension + pytest | `dot_product([1,2,3],[4,5,6])` returns `15` instead of `32` | `039259b` | `cd python-cpp && rm -rf build/ *.so && python setup.py develop 2>&1 && python -m pytest tests/` |
| [pip-django](pip-django/README.md) | pip + Django + pytest | `word_count("hello world")` returns `11` instead of `2` | `170db6b` | `cd pip-django && find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; pip install -r requirements.txt -q --break-system-packages && pytest tests/` |
| [deno-nextjs](deno-nextjs/README.md) | Deno + Next.js | `chunk([1,2,3,4,5], 2)` returns single-item chunks | `afabe47` | `cd deno-nextjs && deno test` |
| [ruby-rails](ruby-rails/README.md) | Ruby + Rails + minitest | `titleize("hello world")` returns `"hello world"` instead of `"Hello World"` | `f04f905` | `cd ruby-rails && bundle install --quiet && bundle exec rake test` |
| [dotnet-xunit](dotnet-xunit/README.md) | .NET 8 + xUnit | `Repeat("abc", 3)` returns `"abc"` instead of `"abcabcabc"` | `c348aaf` | `cd dotnet-xunit && dotnet test --no-restore` |

Most exercises use `c8a9b34` as the known-good scaffold commit. A few were added later, and `script.sh` predates the rest of the project, so their starting points differ.

## Picking a First Exercise

If you want the fastest path to a first bisect run:

- Start with `script.sh` if you want the smallest possible example.
- Try `go-test`, `cargo-rust`, or `deno-nextjs` if you want a language-specific exercise with minimal setup.
- Leave `python-cpp` for later; it intentionally includes a rebuild step on every bisect iteration.

## Notes for `git bisect run`

- Exit code `0` means the current commit is good.
- Exit code `125` tells Git to skip the current commit.
- Any other non-zero exit code from `1` to `127` marks the current commit as bad.
- Exit codes `128` and above stop the bisect run because the command itself failed unexpectedly.

<details>
<summary>Spoilers: first bad commits</summary>

| Exercise | First bad commit |
| --- | --- |
| `script.sh` | `cc475dc` |
| `bun-jest` | `ecbff1e` |
| `uv-flask` | `e58d699` |
| `node-vitest` | `5d1808b` |
| `cargo-rust` | `e1dd2bf` |
| `go-test` | `16a6d6d` |
| `python-cpp` | `af07708` |
| `pip-django` | `66005a5` |
| `deno-nextjs` | `5f3e023` |
| `ruby-rails` | `20f29ac` |
| `dotnet-xunit` | `349caf0` |

</details>
