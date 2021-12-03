from django.views import View
from django.shortcuts import render

# Create your views here.


class Index(View):
    """主页视图"""

    def get(self, request, *args, **kwargs):
        data_list = [{"name": "车身等效质量", "value": 1354.5, "unit": "Kg"},
                     {"name": "前轴非悬挂件等效质量", "value": 80, "unit": "Kg"},
                     {"name": "后轴非悬挂件等效质量", "value": 68.5, "unit": "Kg"},
                     {"name": "车身绕质心的转动惯量", "value": 64.3, "unit": "Kg*m2"},
                     {"name": "前悬架系统的等效阻尼系数", "value": 600, "unit": "Ns/m"},
                     {"name": "后悬架系统的等效阻尼系数", "value": 550, "unit": "Ns/m"},
                     {"name": "前悬架系统的等效刚度", "value": 18000, "unit": "N/m"},
                     {"name": "后悬架系统的等效刚度", "value": 16997, "unit": "N/m"},
                     {"name": "前轮胎的等效刚度", "value": 118000, "unit": "N/m"},
                     {"name": "后轮胎的等效刚度", "value": 118000, "unit": "N/m"},
                     {"name": "前轮中心至车架质心的距离", "value": 1.110, "unit": "m"},
                     {"name": "后轮中心至车架质心的距离", "value": 1.300, "unit": "m"},
                     {"name": "汽车前后轴之间距离", "value": 2.410, "unit": "m"}
                     ]
        context = {"data_list": data_list}
        return render(request, 'vibration/initialize.html', context)