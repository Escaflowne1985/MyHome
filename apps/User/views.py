# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View  # 基于类实现需要继承的view
from django.http import HttpResponse

# token认证
from .models import *
from .serilaizes import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication  # jwt用户认证


# JWT 权限设置
class MyPermission(BasePermission):
    message = '自定义的返回信息'

    def has_permission(self, request, view):  # 列表数据
        # # 这个函数返回True或者False，True表示有权限，False表示没有权限,这个函数同时有三个参数，最后一个是view， 这个是在源码中规定的
        # if request.user.id == 0:
        #     return False
        # else:
        return True

    def has_object_permission(self, request, view, obj):  # 对象数据
        """用户是否有权限访问添加了权限控制类的数据对象"""
        # 需求：用户能够访问id为1，3的对象，其他的不能够访问
        if request.user.is_active == 0:
            return True
        else:
            return False


#
class TokenCheckViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, MyPermission)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = UserProfile.objects.all()
    serializer_class = TokenCheckSerializer


import requests


class WeChatLoginView(View):
    def get(selt, request):
        appid = 'wxe50938d2b573b1f8'
        secret = 'd75116ded7d4823490d72450faed1934'
        code = request.GET.get('code')
        weixin_url = requests.get(
            f"https://api.weixin.qq.com/sns/oauth2/access_token?appid={appid}&secret={secret}&code={code}&grant_type=authorization_code")
        info = weixin_url.json()
        open_id = info.get('openid')
        access_token = info.get('access_token')
        user_info_req = requests.get(
            f'https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={open_id}&lang=zh_CN')
        user_info_req.encoding = 'utf-8'
        user_info = user_info_req.json()
        context = {'code': request.GET.get('code'), 'info': info, 'user_info': user_info}
        return render(request, 'test.html', context)


# https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxe50938d2b573b1f8&redirect_uri=https://home.datayang.cn&response_type=code&scope=snsapi_base&state=123#wechat_redirect

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from Account.models import Account
from web_template_0 import settings


@api_view(["GET"])
def wx_login(request):
    # 微信扫码登录接口 微信开放平台配置
    params = {
        "appid": settings.WeiXinWebAppID,
        "secret": settings.WeiXinWebAppSecret,
        "code": request.GET.get("code"),
        "grant_type": "authorization_code"
    }
    res = requests.get("https://api.weixin.qq.com/sns/oauth2/access_token", params=params)
    res = res.json()
    access_token = res["access_token"]
    openid = res["openid"]
    # 获取用户信息
    params = {
        "access_token": access_token,
        "openid": openid,
    }
    res = requests.get("https://api.weixin.qq.com/sns/userinfo", params=params)
    res = res.json()
    # 判断用户是否存在
    account = Account.objects.filter(openid=openid).first()
    if not account:
        # 如果用户不存在，则创建用户
        account = Account.objects.create(
            openid=openid,
            unionId=res["unionid"],
            nickname=res["nickname"],
            headImgUrl=res["headimgurl"]
        )
    # 根据用户信息生成JWT token
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(account)
    token = jwt_encode_handler(payload)
    # 返回用户信息 + token
    return Response({
        "token": token,
        "account": {
            "openid": account.openid,
            "nickname": account.nickname,
            "headImgUrl": account.headImgUrl
        }
    })
