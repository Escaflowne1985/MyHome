# coding:utf-8
from django.urls import path, re_path, include
from django.views.static import serve
from MyHome.settings import *  #
from MyHomePage.views import *
import xadmin

urlpatterns = [
    # 配置adminx后台路由
    path('xadmin/', xadmin.site.urls),
    # 主页的路由地址
    path('', include('MyHomePage.urls', namespace='MyHomePage')),
    path('', include('GameTool.urls', namespace='Comment')),
    path('', include('User.urls', namespace='User')),
    # 配置media的url
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}, name='media'),
    # # static配置云服务器使用
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}, name='static'),
    # 配置markdown编译器路由
    # re_path(r'mdeditor/', include('mdeditor.urls')),
]
