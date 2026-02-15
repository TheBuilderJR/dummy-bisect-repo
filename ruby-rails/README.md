# ruby-rails — Bisect Exercise

## Setup

```bash
cd ruby-rails
bundle install
```

## The Bug

The `titleize` function is broken — `titleize("hello world")` returns `"hello world"` instead of `"Hello World"`. It's lowercasing the whole string instead of capitalizing each word.

## How to Bisect

```bash
git bisect start
git bisect bad HEAD
git bisect good <good-commit>
git bisect run sh -c 'cd ruby-rails && bundle install --quiet && bundle exec rake test'
```

## Test Command

```bash
cd ruby-rails && bundle exec rake test
```

A passing run exits 0. A failing run exits non-zero.

## Notes

Requires Ruby 3.0+ and Bundler. Rails is used for the web layer, but the bisect target is the text helper utilities.

## Answer

The first bad commit is `<bad-commit>` ("Normalize ruby-rails titleize case handling"), which changed `str.strip.split.map(&:capitalize).join(" ")` to `str.strip.downcase`.
