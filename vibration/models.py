from django.db import models
from django.utils.timezone import now

# Create your models here.


# 描述创建时间和修改事件的父类模型
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateField("创建时间",default=now)
    update_time = models.DateField("修改时间",default=now)

    class Meta:
        abstract = True


class SetData(BaseModel):
    """
    提交数据表
    """
    secret_key = models.CharField(verbose_name="密钥",max_length=12,unique=True)
    m3 = models.IntegerField(verbose_name="质心前部车载设备等效质量", default=250)
    m4 = models.IntegerField(verbose_name="质心后部车载设备等效质量", default=350)
    l3 = models.IntegerField(verbose_name="质心前部车载设备质心至车架质心的距离", default=0.5)
    l4 = models.IntegerField(verbose_name="质心后部车载设备质心至车架质心的距离", default=0.6)
    amplitude = models.IntegerField(verbose_name="振动激励正弦函数振幅", default=24254.147)
    frequency = models.IntegerField(verbose_name="振动激励正弦函数频率", default=4000)

    def __str__(self):
        return self.secret_key

    class Meta:
        verbose_name = "提交车载设备数据表"
        verbose_name_plural = "提交车载设备数据表"
        ordering = ["-update_time"]


class InitialPara(models.Model):
    """
    初始化参数表
    """
    id = models.AutoField(primary_key=True)
    m = models.IntegerField(verbose_name="车身等效质量", default=1354.5)
    m1 = models.IntegerField(verbose_name="前轴非悬挂件等效质量", default=80)
    m2 = models.IntegerField(verbose_name="后轴非悬挂件等效质量", default=68.5)
    j = models.IntegerField(verbose_name="车身绕质心的转动惯量", default=64.30)
    c1 = models.IntegerField(verbose_name="前悬架系统的等效阻尼系数", default=600)
    c2 = models.IntegerField(verbose_name="后悬架系统的等效阻尼系数", default=550)
    k1 = models.IntegerField(verbose_name="前悬架系统的等效刚度", default=18000)
    k2 = models.IntegerField(verbose_name="后悬架系统的等效刚度", default=16997)
    k4 = models.IntegerField(verbose_name="前轮胎的等效刚度", default=118000)
    k5 = models.IntegerField(verbose_name="后轮胎的等效刚度", default=118000)
    l1 = models.IntegerField(verbose_name="前轮中心至车架质心的距离", default=1.110)
    l2 = models.IntegerField(verbose_name="后轮中心至车架质心的距离", default=1.300)
    length = models.IntegerField(verbose_name="汽车前后轴之间距离", default=2.410)

    def __str__(self):
        return self.m

    class Meta:
        verbose_name = "初始化参数表"
        verbose_name_plural = "初始化参数表"

