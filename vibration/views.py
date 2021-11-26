from django.views import View
from django.shortcuts import render

# Create your views here.


class Initialization(View):
    """
    参数初始化
    """

    def get(self, request, *args, **kwargs):
        data_list = [{"name": "车身等效质量", "value": 2150, "unit": "Kg"},
                     {"name": "前轴非悬挂件等效质量", "value": 80, "unit": "Kg"},
                     {"name": "后轴非悬挂件等效质量", "value": 80, "unit": "Kg"},
                     {"name": "车身绕质心的转动惯量", "value": 14000, "unit": "Kg*m2"},
                     {"name": "前悬架系统的等效阻尼系数", "value": 3000, "unit": "Ns/m"},
                     {"name": "后悬架系统的等效阻尼系数", "value": 3000, "unit": "Ns/m"},
                     {"name": "前悬架系统的等效刚度", "value": 12000, "unit": "N/m"},
                     {"name": "后悬架系统的等效刚度", "value": 12000, "unit": "N/m"},
                     {"name": "前轮胎的等效刚度", "value": 100000, "unit": "N/m"},
                     {"name": "后轮胎的等效刚度", "value": 100000, "unit": "N/m"},
                     {"name": "前轮中心至车架质心的距离", "value": 1.8, "unit": "m"},
                     {"name": "后轮中心至车架质心的距离", "value": 1.5, "unit": "m"},
                     {"name": "汽车前后轴之间距离", "value": 3.3, "unit": "m"}
                     ]
        context = {"data_list":data_list}

        return render(request, 'main/initialize.html', context)


class Set(View):
    """
    车载设备参数设置
    """
    pass



