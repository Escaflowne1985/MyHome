# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = ''

from django.urls import path
from .views import *

app_name = 'MyHomePage'

urlpatterns = [
    path('Introduction', MyHomeIndex.as_view(), name='MyHomeIndex'),
]
