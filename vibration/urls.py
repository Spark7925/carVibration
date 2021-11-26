#!/usr/bin/env python
# encoding: utf-8

"""
version: 1.0.0
author: binchen
time: 2021-11-25 18:02
"""

from django.conf.urls import url
from vibration.views import Initialization,Set


urlpatterns = [
    url(r'initialize/',Initialization.as_view(),name="initializePara"),
    url(r'set/',Set.as_view(),name="set"),
]