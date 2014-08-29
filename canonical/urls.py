from django.conf.urls import patterns, url
from fenchurch import TemplateFinder
from views import custom_404, custom_500
from django.conf import settings
from django.conf.urls.static import static

# Standard patterns
urlpatterns = patterns(
    '',
    url(r'^(?P<template>.*)/?$', TemplateFinder.as_view()),  # Fenchurch
)

# Static files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Error handlers
handler404 = custom_404
handler500 = custom_500
