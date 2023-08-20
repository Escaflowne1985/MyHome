# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '后端API users的models'

from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户列表模型
class UserProfile(AbstractUser):
    actual_name = models.CharField(max_length=10, verbose_name="用户姓名", null=True, blank=True)
    nick_name = models.CharField(max_length=20, verbose_name="用户昵称", null=True, blank=True)
    Gender = (("Male", "男"), ("Female", "女"), ("Undefined", "未定义"))
    gender = models.CharField(max_length=9, verbose_name="用户性别", choices=Gender, default="未定义")
    birthday = models.DateField(verbose_name="用户生日", null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="联系地址", default="", blank=True)
    mobile = models.CharField(max_length=11, verbose_name="联系电话", null=True, blank=True)
    user_image = models.ImageField(
        upload_to="UserImage", default="UserImage/default.png",
        verbose_name="用户头像", null=True, blank=True
    )
    integral = models.IntegerField(default=0, verbose_name="用户积分", help_text="积分")
    vip_level = models.IntegerField(default=0, verbose_name="用户等级", help_text="等级")
    vip_exp = models.IntegerField(default=0, verbose_name="用户经验", help_text="经验值")
    openid = models.CharField(max_length=100, blank=True, null=True, verbose_name="微信openid", unique=True)

    class Meta:
        verbose_name = "用户信息列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
