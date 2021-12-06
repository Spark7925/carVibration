from django.views import View
from django.views import generic
from django.shortcuts import render
from django.http import JsonResponse

from vibration.forms import EquipmentSetForm, VibrationFuncForm
from vibration.models import SetData, InitialPara

# Create your views here.


# 仿真开始函数
def begin(request):
    ret = {"status": 0, "message": "内部数据错误,请重试!"}
    if request.method == "POST":
        secret_key = request.POST.get("secret_key", None)
        if secret_key:
            request.session["secret_key"] = secret_key
            SetData.objects.create(**{"secret_key": secret_key})
            ret["status"] = 1
            ret["message"] = ""
            return JsonResponse(ret)
    return JsonResponse(ret)


# 参数初始化设置
def para_set(request):
    para_set_ret = {"status": 0, "message": "参数初始化失败,请重试!"}
    if request.method == "POST":
        initial_para_data = {
            "m": 1354.5,
            "m1": 80,
            "m2": 68.5,
            "j": 64.3,
            "c1": 600,
            "c2": 550,
            "k1": 18000,
            "k2": 16997,
            "k4": 118000,
            "k5": 118000,
            "l1": 1.110,
            "l2": 1.300,
            "length": 2.410
        }
        initialize_valid = request.POST.get("initialize_valid", None)
        if initialize_valid:
            initial_para_obj = InitialPara.objects.all()
            if initial_para_obj:
                pass
            else:
                InitialPara.objects.create(**initial_para_data)
            para_set_ret["status"] = 1
            para_set_ret["message"] = "参数初始化成功，请进行下一步！"
            return JsonResponse(para_set_ret)
    return JsonResponse(para_set_ret)


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
        context = {"data_list": data_list}

        return render(request, 'vibration/initialize.html', context)


# 用户设置车载设备参数
class EquipmentSet(generic.FormView):
    """
    车载设备参数设置
    """
    form_class = EquipmentSetForm
    template_name = 'vibration/equipment_set.html'
    success_url = '/vibration/equipment_set/'

    def form_valid(self, form):
        secret_key = self.request.session['secret_key']
        set_data_obj = SetData.objects.get(secret_key=secret_key)
        if set_data_obj:
            set_data_obj.m3 = form.cleaned_data['m3']
            set_data_obj.m4 = form.cleaned_data['m4']
            set_data_obj.l3 = form.cleaned_data['l3']
            set_data_obj.l4 = form.cleaned_data['l4']
            set_data_obj.save()
        else:
            kwargs = {
                'm3': form.cleaned_data['m3'],
                'm4': form.cleaned_data['m4'],
                'l3': form.cleaned_data['l3'],
                'l4': form.cleaned_data['l4'],
                'secret_key': secret_key
            }
            set_data_obj.objects.create(**kwargs)

        return super(EquipmentSet, self).form_valid(form)


# 用户设置振动激励函数参数
class VibrationFunc(generic.FormView):
    """
    振动激励函数参数设置
    """
    form_class = VibrationFuncForm
    template_name = 'vibration/vibration_func.html'
    success_url = '/vibration/vibration_func/'

    def form_valid(self, form):
        secret_key = self.request.session['secret_key']
        set_data_obj = SetData.objects.get(secret_key=secret_key)
        if set_data_obj:
            set_data_obj.amplitude = form.cleaned_data['amplitude']
            set_data_obj.frequency = form.cleaned_data['frequency']
            set_data_obj.save()
        else:
            kwargs = {
                'amplitude': form.cleaned_data['amplitude'],
                'frequency': form.cleaned_data['frequency'],
                'secret_key': secret_key
            }
            set_data_obj.objects.create(**kwargs)

        return super(VibrationFunc, self).form_valid(form)


# 仿真参数检查
def para_valid(request):
    para_valid_ret = {"status": 0, "message": "参数检查错误,请检查已完成的步骤!"}
    if request.method == "POST":
        secret_key = request.POST.get("secret_key", None)
        if secret_key:
            set_data_obj = SetData.objects.get(secret_key=secret_key)
        else:
            return JsonResponse(para_valid_ret)
        initial_data_obj = InitialPara.objects.get(id=1)
        if set_data_obj and initial_data_obj:
            para_valid_ret["status"] = 1
            para_valid_ret["message"] = "参数检查成功，请进行下一步！"
            return JsonResponse(para_valid_ret)
    return JsonResponse(para_valid_ret)


# 仿真开始函数
def simulate(request):
    simulate_ret = {"status": 0, "message": "仿真计算失败,请检查之前的步骤!"}
    if request.method == "POST":
        secret_key = request.POST.get("secret_key", None)
        if secret_key:
            # try:
            set_data_obj = SetData.objects.get(secret_key=secret_key)
            initial_para_obj = InitialPara.objects.get(id=1)
            # simulate_data = {
            #     "secret_key": set_data_obj.secret_key,
            #     "m3": set_data_obj.m3,
            #     "m4": set_data_obj.m4,
            #     "l3": set_data_obj.l3,
            #     "l4": set_data_obj.l4,
            #     "amplitude": set_data_obj.amplitude,
            #     "frequency": set_data_obj.frequency,
            #     "m": initial_para_obj.m,
            #     "m1": initial_para_obj.m1,
            #     "m2": initial_para_obj.m2,
            #     "j": initial_para_obj.j,
            #     "c1": initial_para_obj.c1,
            #     "c2": initial_para_obj.c2,
            #     "k1": initial_para_obj.k1,
            #     "k2": initial_para_obj.k2,
            #     "k4": initial_para_obj.k4,
            #     "k5": initial_para_obj.k5,
            #     "l1": initial_para_obj.l1,
            #     "l2": initial_para_obj.l2,
            #     "length": initial_para_obj.length
            # }

            # python数据转化为matlab可以接收的数据类型
            matlab_m3 = set_data_obj.m3
            matlab_m3 = float(matlab_m3)
            matlab_m4 = set_data_obj.m4
            matlab_m4 = float(matlab_m4)
            matlab_l3 = set_data_obj.l3
            matlab_l3 = float(matlab_l3)
            matlab_l4 = set_data_obj.l4
            matlab_l4 = float(matlab_l4)
            matlab_amplitude = set_data_obj.amplitude
            matlab_amplitude = float(matlab_amplitude)
            matlab_frequency = set_data_obj.frequency
            matlab_frequency = float(matlab_frequency)

            # 调用MATLAB引擎，计算求解
            import matlab.engine
            engine = matlab.engine.start_matlab()
            engine.python_middle_matlab(matlab_m3, matlab_m4, matlab_l3, matlab_l4, matlab_amplitude, matlab_frequency)

            # except Exception as e:
            #     return JsonResponse(simulate_ret)

            simulate_ret["status"] = 1
            simulate_ret["message"] = "计算完成！"
            return JsonResponse(simulate_ret)
    return JsonResponse(simulate_ret)






