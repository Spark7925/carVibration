#!/usr/bin/env python
# encoding: utf-8

"""
version: 1.0.0
author: binchen
time: 2021-11-26 10:05
"""

from django.conf.urls import url
from main.views import Index


urlpatterns = [
    url(r'index/',Index.as_view(),name="index"),
]