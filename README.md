# Git Bisect Practice Repo

This repository is a collection of small, intentionally broken projects for practicing `git bisect`.

Each exercise lives in its own directory, has one known regression somewhere in the commit history, and includes a focused test command you can use with `git bisect run`.

## What This Repo Is For

Use this repo if you want to practice:

- narrowing a regression down to the first bad commit
- automating `git bisect` with a repeatable test command
- working across different stacks without needing a large codebase

The projects are small on purpose. The point is to learn the bisect workflow, not fight setup complexity.

## Quick Start

1. Pick an exercise from the table below.
2. Run its setup command if needed.
3. Confirm the current `HEAD` is failing with the listed test command.
4. Start a bisect session:

```bash
git bisect start
git bisect bad HEAD
git bisect good <known-good-commit>
git bisect run sh -c '<exercise test command>'
```

5. When Git reports the first bad commit, reset:

```bash
git bisect reset
```

## Exercises

| Exercise | Stack | Regression | Setup | Test Command | Known Good |
|----------|-------|------------|-------|--------------|------------|
| `script.sh` | Bash | exits `1` instead of `0` | none | `./script.sh` | `c8a9b34` |
| `bun-jest/` | Bun + Jest | `multiply` returns the wrong result | `cd bun-jest && bun install` | `cd bun-jest && bun test` | `c8a9b34` |
| `uv-flask/` | uv + Flask + pytest | `add` subtracts instead of adding | `cd uv-flask && uv sync --extra dev` | `cd uv-flask && uv run pytest tests/` | `c8a9b34` |
| `node-vitest/` | Node + Vitest | `capitalize` lowercases instead | `cd node-vitest && npm install` | `cd node-vitest && npx vitest run` | `c8a9b34` |
| `cargo-rust/` | Rust + cargo test | `reverse_string` stops reversing | `cd cargo-rust` | `cd cargo-rust && cargo test` | `c8a9b34` |
| `go-test/` | Go + go test | `Divide` multiplies instead of dividing | `cd go-test` | `cd go-test && go test ./...` | `c8a9b34` |
| `python-cpp/` | Python + C++ extension + pytest | `dot_product` adds instead of multiplies | `cd python-cpp` | `cd python-cpp && rm -rf build/ *.so && python setup.py develop 2>&1 && python -m pytest tests/` | `039259b` |
| `pip-django/` | pip + Django + pytest | `word_count` counts characters instead of words | `cd pip-django && pip install -r requirements.txt -q` | `cd pip-django && find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; pytest tests/` | `170db6b` |
| `deno-nextjs/` | Deno + Next.js | `chunk` ignores the requested chunk size | `cd deno-nextjs` | `cd deno-nextjs && deno test` | `afabe47` |
| `ruby-rails/` | Ruby + Rails + minitest | `titleize` lowercases instead of title-casing | `cd ruby-rails && bundle install --quiet` | `cd ruby-rails && bundle exec rake test` | `f04f905` |
| `dotnet-xunit/` | .NET 8 + xUnit | `Repeat` only repeats once | `cd dotnet-xunit` | `cd dotnet-xunit && dotnet test` | `c348aaf` |

## Example

To bisect the bug in `go-test/`:

```bash
git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd go-test && go test ./...'
```

Git will checkout commits for you, run the test each time, and stop at the first bad commit.

## Notes

- Some exercises were added later in history, so their known-good commit is newer than `c8a9b34`.
- The `python-cpp/` exercise rebuilds the extension on each bisect step so you do not get stale compiled artifacts.
- Each exercise directory has its own `README.md` with setup details, bisect commands, and the answer if you want to check your work.

## Where To Go Next

If you want a guided exercise, start with one of these:

- `script.sh` for the fastest possible bisect
- `go-test/` or `bun-jest/` for a simple test-driven workflow
- `python-cpp/` for a case where build artifacts matter during bisect

If you want the solutions, open the README inside the exercise directory you chose.
