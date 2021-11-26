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


class SubmitData(BaseModel):
    """
    提交数据表
    """
    secret_key = models.CharField(verbose_name="密钥",max_length=12,unique=True)
    m3 = models.IntegerField(verbose_name="质心前部车载设备等效质量", default=1.8)
    m4 = models.IntegerField(verbose_name="质心后部车载设备等效质量", default=1.5)
    l3 = models.IntegerField(verbose_name="质心前部车载设备质心至车架质心的距离", default=100)
    l4 = models.IntegerField(verbose_name="质心后部车载设备质心至车架质心的距离", default=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "提交数据表"
        verbose_name_plural = "提交数据表"
        ordering = ["-update_time"]
        get_latest_by = "id"