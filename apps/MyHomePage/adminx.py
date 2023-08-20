# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = '我的主页adminx后台配置文件'

from .models import *
import xadmin


# 我的基本信息
class MyInformationAdmin(object):
    list_display = ['full_name', 'age', 'email']
    show_bookmarks = False


class EducationExperienceListAdmin(object):
    list_display = ['education_experience_type', 'name', 'duration_time', 'info', ]
    show_bookmarks = False


class MyServiceProjectTypeAdmin(object):
    list_display = ['type_en', 'type_cn']
    show_bookmarks = False


class MyServiceProjectListAdmin(object):
    list_display = ['type_name', 'title', 'info', 'url']
    show_bookmarks = False


class MyBlogListAdmin(object):
    list_display = ['title', 'info', 'url', ]
    show_bookmarks = False


# 联系我的信息
class ContactMeAdmin(object):
    list_display = ['subject', 'email', 'add_time', ]
    show_bookmarks = False


xadmin.site.register(MyInformation, MyInformationAdmin)
xadmin.site.register(EducationExperienceList, EducationExperienceListAdmin)
xadmin.site.register(MyServiceProjectType, MyServiceProjectTypeAdmin)
xadmin.site.register(MyServiceProjectList, MyServiceProjectListAdmin)
xadmin.site.register(MyBlogList, MyBlogListAdmin)
xadmin.site.register(ContactMe, ContactMeAdmin)
