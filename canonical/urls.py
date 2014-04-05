from django.conf.urls import patterns, url
from fenchurch import TemplateFinder
from views import custom_404, custom_500

urlpatterns = patterns('',
    url(r'^(?P<template>.*)$', TemplateFinder.as_view()),
)

handler404 = custom_404
handler500 = custom_500
