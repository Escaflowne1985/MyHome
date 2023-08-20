# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'User 应用 serializes API 序列化配置'

from .models import *
from rest_framework import serializers


# 用户列表
class TokenCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ["is_superuser", "first_name", "last_name", "is_staff", "groups", "user_permissions"]
