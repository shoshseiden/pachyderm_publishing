from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from .forms import ReviewForm
from .models import Book, Genre, Author


class GenreView(generic.ListView):

    template_name = "genre.html"
    context_object_name = "genre_list"

    def queryset(self):
        return Genre.objects.order_by('genre_name')


class AuthorView(generic.ListView):
    template_name = "author.html"
    context_object_name = "author_list"

    def queryset(self):
        return Author.objects.order_by('author_formatted_name')


class LibraryByGenreView(generic.DetailView):

    model = Genre
    template_name = "library_by_genre.html"


def library_by_author(request, author_id):
    template_name = "library_by_author.html"
    selected_author = get_object_or_404(Author, pk=author_id)
    ctx = {'author': selected_author}
    return render(request, template_name, ctx)


class LibraryView(generic.ListView):
    template_name = "library.html"
    context_object_name = "book_list"

    def queryset(self):
        return Book.objects.order_by('book_title')


def book(request, book_id):
    template_name = "book.html"
    selected_book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
    else:
        review_form = ReviewForm()
    ctx = {'book': selected_book, 'review_form': review_form}
    return render(request, template_name, ctx)


class MissionView(generic.TemplateView):

    template_name = "mission.html"


class ContactView(generic.TemplateView):

    template_name = "contact.html"
