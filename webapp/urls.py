from django.conf.urls import url
from views import CanonicalTemplateFinder, custom_404, custom_500

# Standard patterns
urlpatterns = [
    url(r'^(?P<template>.*)/?$', CanonicalTemplateFinder.as_view()),  # Fenchurch
]

# Error handlers
handler404 = custom_404
handler500 = custom_500
