from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib import admin


urlpatterns = [
    "",
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
]
