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
