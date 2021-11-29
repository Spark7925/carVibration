#!/usr/bin/env python
# encoding: utf-8

"""
version: 1.0.0
author: binchen
time: 2021-11-25 18:02
"""

from django.conf.urls import url
from vibration.views import Initialization, EquipmentSet, begin, VibrationFunc


urlpatterns = [
    url(r'begin/', begin, name="begin"),
    url(r'initialize/', Initialization.as_view(), name="initialize"),
    url(r'equipment_set/', EquipmentSet.as_view(), name="equipment_set"),
    url(r'vibration_func/', VibrationFunc.as_view(), name="vibration_func"),
]