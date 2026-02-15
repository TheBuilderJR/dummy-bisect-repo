"""URL configuration for the pip-django text utilities app."""

from django.http import JsonResponse
from django.urls import path

from utils import word_count, truncate, excerpt, slugify


def index(request):
    return JsonResponse({"status": "ok"})


def word_count_view(request):
    text = request.GET.get("text", "")
    return JsonResponse({"result": word_count(text)})


def truncate_view(request):
    text = request.GET.get("text", "")
    max_length = int(request.GET.get("max_length", 100))
    return JsonResponse({"result": truncate(text, max_length)})


def excerpt_view(request):
    text = request.GET.get("text", "")
    max_words = int(request.GET.get("max_words", 10))
    return JsonResponse({"result": excerpt(text, max_words)})


def slugify_view(request):
    text = request.GET.get("text", "")
    return JsonResponse({"result": slugify(text)})


urlpatterns = [
    path("", index),
    path("word_count", word_count_view),
    path("truncate", truncate_view),
    path("excerpt", excerpt_view),
    path("slugify", slugify_view),
]
