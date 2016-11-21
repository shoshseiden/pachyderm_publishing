import datetime

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from .forms import ReviewForm
from .models import Book, Genre, Author, Review


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
    review_form = ReviewForm()
    ctx = {'book': selected_book, 'review_form': review_form}
    return render(request, template_name, ctx)


def add_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        book_rating = review_form.cleaned_data['book_rating']
        book_review = review_form.cleaned_data['book_review']
        user_name = review_form.cleaned_data['user_name']
        review = Review()
        review.book = book
        review.user_name = user_name
        review.book_rating = book_rating
        review.book_review = book_review
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after sucessfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the back button.
        return HttpResponseRedirect(reverse('book', args=(book.id,)))

    return render(request, 'book.html', {'book': book, 'review_form': review_form})


class MissionView(generic.TemplateView):

    template_name = "mission.html"


class ContactView(generic.TemplateView):

    template_name = "contact.html"
