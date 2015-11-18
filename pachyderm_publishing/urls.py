from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r'^genre/$', views.GenreView.as_view(), name='genre')
]
