#coding: utf-8

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url


urlpatterns = patterns('main.views',
    url(r'^$', 'index'),
    url(r'^(?P<id>\w+)/?$', 'long_url'),
    url(r'^get/short/url/?$', 'short_url'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
