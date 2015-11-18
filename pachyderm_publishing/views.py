from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from .models import Book, Genre, Author


class GenreView(generic.ListView):
    template_name = "genre.html"
    context_object_name = "genre_list"

    def queryset(self):
        return Genre.objects.order_by('genre_name')


def library_by_genre(request, genre_id):
    template_name = "library_by_genre.html"
    selected_genre = get_object_or_404(Genre, pk=genre_id)
    ctx = {'genre': selected_genre}
    return render(request, template_name, ctx)


def book(request, book_id):
    template_name = "book.html"
    selected_book = get_object_or_404(Book, pk=book_id)
    ctx = {'book': selected_book}
    return render(request, template_name, ctx)
