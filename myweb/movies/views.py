from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, "movies/index.html")


def spirited_away_comments(request, comment_id):
    return render(request, "movies/spirited_away/%s.html" % comment_id)


def spirited_away_index(request):
    return render(request, "movies/spirited_away/index.html")


def nezha_index(request):
    return render(request, "movies/NeZha/index.html")


def nezha_comments(request, comment_id):
    return render(request, "movies/NeZha/%s.html" % comment_id)
# Create your views here.
