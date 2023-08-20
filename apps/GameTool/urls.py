# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = ''

from django.urls import path, re_path
from .views import *

app_name = 'GameTool'

urlpatterns = [
    # 《三国无双20周年纪念》人物羁绊计算
    path('SanGuoRenWuJiBan', SanGuoRenWuJiBanView.as_view(), name='SanGuoRenWuJiBan'),
]
