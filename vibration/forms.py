#!/usr/bin/env python
# encoding: utf-8

"""
version: 2.0.0
author: binchen
time: 2021-12-09 11:29
注册功能用到的form类
"""

from django import forms
from django.core.exceptions import ValidationError


# 定义一个提交车载设备数据的form类
class EquipmentSetForm(forms.Form):
    m3 = forms.DecimalField(
        label="质心前部车载设备等效质量",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    m4 = forms.DecimalField(
        label="质心后部车载设备等效质量",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    l3 = forms.DecimalField(
        label="质心前部车载设备质心至车架质心的距离",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    l4 = forms.DecimalField(
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
    amplitude = forms.DecimalField(
        label="振动激励正弦函数振幅",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    frequency = forms.DecimalField(
        label="振动激励发动机转速",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )


# 定义一个设置减震器参数的form类
class AbsorberForm(forms.Form):
    k7 = forms.DecimalField(
        label="质心前部车载设备减震器刚度系数",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    k8 = forms.DecimalField(
        label="质心后部车载设备减震器刚度系数",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    c5 = forms.DecimalField(
        label="质心前部车载设备减震器阻尼系数",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    c6 = forms.DecimalField(
        label="质心后部车载设备减震器阻尼系数",
        error_messages={
            "required": "数据不能为空",
        },

        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )


