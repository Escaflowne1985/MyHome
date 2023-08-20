# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = 'User 应用 Adminx 后台管理控制配置'

from django.contrib.auth import get_user_model
import xadmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import *
from xadmin.layout import *




# 用户信息管理
class UserProfileAdmin(object):
    list_display = ['username', 'user_role', 'nick_name', 'integral', 'email']
    readonly_fields = ['date_joined', 'last_login']
    show_bookmarks = False

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('用户信息',
                             'username', 'actual_name', 'nick_name', 'gender',
                             'address', 'mobile', 'email', 'birthday',
                             ),
                    Fieldset(('用户数据'),
                             Row('integral', 'vip_level', 'vip_exp'),
                             Row('last_login', 'date_joined'),
                             ),
                    Fieldset(None,
                             'password', 'user_permissions', 'first_name', 'last_name',
                             **{"style": "display:None"}),
                ),
                Side(
                    Fieldset(('用户'),
                             'user_image',
                             ),
                    Fieldset(('用户权限'),
                             'groups',
                             ),
                    Fieldset(('用户身份'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserProfileAdmin, self).get_form_layout()
