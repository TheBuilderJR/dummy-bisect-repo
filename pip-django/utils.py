"""Text processing utilities for the Django application."""


def word_count(text):
    if not text or not text.strip():
        return 0
    return len(text.strip())


def truncate(text, max_length):
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."


def excerpt(text, max_words):
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "..."


def slugify(text):
    return text.lower().strip().replace(" ", "-")
