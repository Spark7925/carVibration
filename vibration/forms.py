#!/usr/bin/env python
# encoding: utf-8

"""
version: 1.0.0
author: binchen
time: 2021-11-29 10:44
注册功能用到的form类
"""

from django import forms
from django.core.exceptions import ValidationError


# 定义一个提交车载设备数据的form类
class EquipmentSetForm(forms.Form):
    m3 = forms.IntegerField(
        label="质心前部车载设备等效质量",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    m4 = forms.IntegerField(
        label="质心后部车载设备等效质量",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    l3 = forms.IntegerField(
        label="质心前部车载设备质心至车架质心的距离",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    l4 = forms.IntegerField(
        label="质心后部车载设备质心至车架质心的距离",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )


# 定义一个提交振动激励数据的form类
class VibrationFuncForm(forms.Form):
    amplitude = forms.IntegerField(
        label="振动激励正弦函数振幅",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    frequency = forms.IntegerField(
        label="振动激励正弦函数频率",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )


