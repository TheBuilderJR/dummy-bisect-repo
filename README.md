# Git Bisect Practice Repo

Practice `git bisect` across small, intentionally broken projects in different stacks. Each exercise has a known-good commit, a later bug-introducing commit, and a test command you can automate with `git bisect run`.

The goal is simple: pick an exercise, mark the current state as bad, mark the scaffold commit as good, and let Git narrow the search for the first bad commit.

## Quick Start

Use the repository root for `git bisect`, even when the test command runs inside a subdirectory.

```bash
# Example: bun-jest
cd bun-jest
bun install
cd ..

git bisect start
git bisect bad HEAD
git bisect good c8a9b34
git bisect run sh -c 'cd bun-jest && bun test'

git bisect reset
```

## Exercise Catalog

Each exercise directory has its own `README.md` with setup notes and the exact bisect command. If you want to avoid spoilers, stop before the `Answer` section.

| Exercise | Stack | What is broken | Good commit | Test command |
|----------|-------|----------------|-------------|--------------|
| `script.sh` | Bash | script exits `1` instead of `0` | `e77a9a5` | `./script.sh` |
| `bun-jest/` | Bun + Jest | `multiply` returns the wrong result | `c8a9b34` | `cd bun-jest && bun test` |
| `uv-flask/` | uv + Flask + pytest | `add` subtracts instead of adding | `c8a9b34` | `cd uv-flask && uv run pytest tests/` |
| `node-vitest/` | Node + Vitest | `capitalize` lowercases instead | `c8a9b34` | `cd node-vitest && npx vitest run` |
| `cargo-rust/` | Rust + cargo test | `reverse_string` no longer reverses | `c8a9b34` | `cd cargo-rust && cargo test` |
| `go-test/` | Go + go test | `Divide` multiplies instead | `c8a9b34` | `cd go-test && go test ./...` |
| `python-cpp/` | Python + C++ extension + pytest | `dot_product` adds instead of multiplying | `039259b` | `cd python-cpp && rm -rf build/ *.so && python setup.py develop 2>&1 && python -m pytest tests/` |
| `pip-django/` | pip + Django + pytest | `word_count` counts characters instead of words | `170db6b` | `cd pip-django && find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; pip install -r requirements.txt -q && pytest tests/` |
| `deno-nextjs/` | Deno + Next.js | `chunk` ignores the requested chunk size | `afabe47` | `cd deno-nextjs && deno test` |
| `ruby-rails/` | Ruby + Rails + minitest | `titleize` lowercases instead of title-casing | `f04f905` | `cd ruby-rails && bundle install --quiet && bundle exec rake test` |
| `dotnet-xunit/` | .NET 8 + xUnit | `Repeat` only repeats once | `c348aaf` | `cd dotnet-xunit && dotnet test` |

## Suggested Workflow

1. Pick an exercise from the table above.
2. Open that exercise's README and install only what it needs.
3. Start bisecting from the repository root.
4. Use the exercise's good commit and test command.
5. When Git reports the first bad commit, inspect it and then run `git bisect reset`.

## Tips

- Start with `script.sh` if you want the fastest no-dependency exercise.
- Most exercises use `c8a9b34` as the good scaffold commit, but newer exercises were added later and have different good commits.
- If a test leaves build artifacts behind, keep the test command exactly as documented so each bisect step runs cleanly.
- If you want to inspect the history yourself, `git log --oneline --decorate` is usually enough.

## Spoilers

The per-exercise READMEs include the answer. If you want a root-level answer key, expand this section.

<details>
<summary>Show first bad commits</summary>

| Exercise | First bad commit | Commit message |
|----------|------------------|----------------|
| `script.sh` | `cc475dc` | `Update exit code` |
| `bun-jest/` | `ecbff1e` | `Update bun-jest multiply with rounding adjustment` |
| `uv-flask/` | `e58d699` | `Refactor uv-flask arithmetic helpers` |
| `node-vitest/` | `5d1808b` | `Normalize node-vitest capitalize for consistency` |
| `cargo-rust/` | `e1dd2bf` | `Simplify cargo-rust reverse_string implementation` |
| `go-test/` | `16a6d6d` | `Optimize go-test Divide for performance` |
| `python-cpp/` | `af07708` | `Optimize python-cpp dot_product accumulation` |
| `pip-django/` | `66005a5` | `Refine pip-django word_count whitespace handling` |
| `deno-nextjs/` | `5f3e023` | `Optimize deno-nextjs chunk iteration step` |
| `ruby-rails/` | `20f29ac` | `Normalize ruby-rails titleize case handling` |
| `dotnet-xunit/` | `349caf0` | `Streamline dotnet-xunit Repeat loop logic` |

</details>
