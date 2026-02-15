from utils import word_count, truncate, excerpt, slugify


def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("one") == 1
    assert word_count("the quick brown fox") == 4
    assert word_count("") == 0
    assert word_count("   ") == 0


def test_truncate():
    assert truncate("hello", 10) == "hello"
    assert truncate("hello world", 5) == "hello..."
    assert truncate("abcdef", 3) == "abc..."


def test_excerpt():
    assert excerpt("the quick brown fox", 2) == "the quick..."
    assert excerpt("hello world", 5) == "hello world"
    assert excerpt("one two three four five", 3) == "one two three..."


def test_slugify():
    assert slugify("Hello World") == "hello-world"
    assert slugify("  foo bar  ") == "foo-bar"
    assert slugify("UPPER CASE") == "upper-case"
