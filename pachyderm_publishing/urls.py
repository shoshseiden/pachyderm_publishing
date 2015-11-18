from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^genre/$', views.GenreView.as_view(), name='genre'),
    url(r'^genre/(?P<genre_id>[0-9]+)/$', views.library_by_genre, name='genre_library'),
    url(r'^author/$', views.AuthorView.as_view(), name='author'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.library_by_author, name='author_library'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.book, name='book'),
]
