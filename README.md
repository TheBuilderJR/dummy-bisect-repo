# Git Bisect Practice Repo

A repository designed for practicing `git bisect`. Each subdirectory simulates a different developer environment where a bug was introduced somewhere in the commit history. Your job: use `git bisect` to find the offending commit.

## Exercises

| Directory | Stack | Bug | Test Command |
|-----------|-------|-----|-------------|
| `script.sh` (root) | Bash | `exit 1` instead of `exit 0` | `./script.sh` |
| `bun-jest/` | Bun + Jest | `multiply` returns wrong result | `cd bun-jest && bun test` |
| `uv-flask/` | uv + Flask + pytest | `add` returns wrong result | `cd uv-flask && uv run pytest tests/` |
| `node-vitest/` | Node + Vitest | `capitalize` lowercases instead | `cd node-vitest && npx vitest run` |
| `cargo-rust/` | Rust + cargo test | `reverse_string` doesn't reverse | `cd cargo-rust && cargo test` |
| `go-test/` | Go + go test | `Divide` multiplies instead | `cd go-test && go test ./...` |
| `python-cpp/` | Python + C++ ext + pytest | `dot_product` adds instead of multiplies | `cd python-cpp && rm -rf build/ *.so && python setup.py develop 2>&1 && python -m pytest tests/` |
| `pip-django/` | pip + Django + pytest | `word_count` counts chars instead of words | `cd pip-django && find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null; pip install -r requirements.txt -q && pytest tests/` |
| `deno-nextjs/` | Deno + Next.js | `chunk` ignores chunk size | `cd deno-nextjs && deno test` |
| `ruby-rails/` | Ruby + Rails + minitest | `titleize` lowercases instead of title-casing | `cd ruby-rails && bundle install --quiet && bundle exec rake test` |

## How Git Bisect Works

```bash
# 1. Start bisecting
git bisect start

# 2. Mark current state as bad
git bisect bad HEAD

# 3. Mark the initial scaffold commit as good (all tests passed here)
#    For most exercises:
git bisect good c8a9b34
#    For python-cpp (which was added later):
#    git bisect good 039259b
#    For pip-django (which was added later):
#    git bisect good 170db6b
#    For deno-nextjs (which was added later):
#    git bisect good afabe47
#    For ruby-rails (which was added later):
#    git bisect good f04f905

# 4. Automate with the test command for your chosen exercise
git bisect run sh -c '<test command from table above>'

# 5. Git will report the first bad commit. Reset when done:
git bisect reset
```

## Commit History Overview

```
06c67b6  Add TODO comment for future ruby-rails enhancements
20f29ac  Normalize ruby-rails titleize case handling              ← BUG (ruby-rails)
af504bb  Add notes section to ruby-rails README
00b1690  Add module docstring to ruby-rails text helpers
f04f905  Add ruby-rails scaffold with Rails app and passing tests ← TESTS PASS (ruby-rails)
75c2787  Add TODO comment for future deno-nextjs enhancements
2a95932  Add notes section to deno-nextjs README
5f3e023  Optimize deno-nextjs chunk iteration step                ← BUG (deno-nextjs)
a18c75f  Add doc comments to deno-nextjs array utilities
afabe47  Add deno-nextjs scaffold with Deno app and passing tests ← TESTS PASS (deno-nextjs)
7967497  Update READMEs with pip-django bisect instructions
cb5a41a  Add TODO comment for future pip-django enhancements
3705a1b  Add module docstring to pip-django views
66005a5  Refine pip-django word_count whitespace handling          ← BUG (pip-django)
190a96d  Add notes section to pip-django README
5108725  Add module docstring to pip-django utils
170db6b  Add pip-django scaffold with Django app and passing tests ← TESTS PASS (pip-django)
04d5b8d  Update root README commit history with latest hashes
83d518b  Fix python-cpp bisect command to force rebuild on each step
b63e5d0  Update READMEs with python-cpp bisect instructions
f8b2b38  Add notes section to python-cpp README
af07708  Optimize python-cpp dot_product accumulation             ← BUG (python-cpp)
62d4540  Add doc comments to python-cpp C++ extension
039259b  Add python-cpp scaffold with C++ extension and passing tests  ← TESTS PASS (python-cpp)
dd1fba8  Update READMEs with bisect instructions and add root README
5614e9c  Add .gitignore for common build artifacts
09fd017  Add TODO comments for future enhancements
5d1808b  Normalize node-vitest capitalize for consistency       ← BUG (node-vitest)
72537f6  Add notes section to uv-flask README
16a6d6d  Optimize go-test Divide for performance                ← BUG (go-test)
4335660  Add package comment to go-test math
e1dd2bf  Simplify cargo-rust reverse_string implementation      ← BUG (cargo-rust)
3ddf86c  Add doc comments to cargo-rust public functions
ecbff1e  Update bun-jest multiply with rounding adjustment      ← BUG (bun-jest)
9fed3cf  Add module comment to node-vitest strings
e58d699  Refactor uv-flask arithmetic helpers                   ← BUG (uv-flask)
db54c93  Add notes section to go-test README
bcdbc41  Add module docstring to bun-jest math utils
c8a9b34  Add project scaffolds with passing tests               ← ALL TESTS PASS
cc475dc  Update exit code                                       ← BUG (script.sh)
db09c77  Add date comment
ab96665  Add author comment
4539172  Add description comment
e77a9a5  Initial commit: add script.sh that echoes hello
```

Each exercise directory has its own README with setup instructions, the exact bisect commands, and the answer.
