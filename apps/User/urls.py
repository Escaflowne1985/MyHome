# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = 'User 应用部分路由设置'

from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import path, re_path
from .views import *
from rest_framework.routers import DefaultRouter

# 自动生成路由方法
router = DefaultRouter()
# apps.users 下的全部路由方法
router.register('TokenCheck', TokenCheckViewSet, "TokenCheck")  # 验证token是否可用

app_name = 'User'

urlpatterns = [
    # path('user_token/',CreateUserTokenViewSet.as_view(),name="user_token"),# 用户Token
    path('token_login/', obtain_jwt_token),  # 获取token，登录视图
    path('token_refresh/', refresh_jwt_token),  # 刷新token
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # 认证地址
    path('WeChatLogin/', WeChatLoginView.as_view(), name='WeChatLogin'),  # 认证地址
]
urlpatterns += router.urls  # 模块地址
