from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static  #Imported for images and css to work.

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^genre/$', views.GenreView.as_view(), name='genre'),
    url(r'^genre/(?P<pk>[0-9]+)/$', views.LibraryByGenreView.as_view(), name='genre_library'),
    url(r'^author/$', views.AuthorView.as_view(), name='author'),
    url(r'^author/(?P<author_id>[0-9]+)/$', views.library_by_author, name='author_library'),
    url(r'^library/$', views.LibraryView.as_view(), name='library'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.book, name='book'),
    url(r'^book/(?P<book_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^mission/$', views.MissionView.as_view(), name='mission'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^pricing/$', views.PriceView.as_view(), name='pricing'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
