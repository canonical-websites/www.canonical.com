from django.conf.urls import url
from django_json_redirects import load_redirects
from .views import CanonicalTemplateFinder, GreenhouseVacancies

urlpatterns = load_redirects() + [
    url(r'^careers/vacancies?$', GreenhouseVacancies.as_view()),
    url(r'^(?P<template>.*)/?$', CanonicalTemplateFinder.as_view())
]
