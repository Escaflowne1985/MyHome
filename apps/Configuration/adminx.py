# -*- coding: utf-8 -*-
__author__ = 'Mr数据杨'
__explain__ = '我的主页adminx后台配置文件'

from MyHomePage.adminx import *
import xadmin
from xadmin import views


# xadmin后台全局设置 主题功能开启
class BaseSetting(object):
    enable_themes = True  # 启用后台主题
    use_bootswatch = True  # 切换主题模式


# xadmin后台菜单设置
class GlobalSettings(object):
    site_title = "我的个人主页"  # 设置站点标题
    site_footer = "Mr数据杨制作"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

    def get_site_menu(self):
        MyHomePageMenu = {'title': '主页管理', 'menus': (
            {'title': '个人介绍', 'url': self.get_model_url(MyInformation, 'changelist')},
            {'title': '教育&职业列表', 'url': self.get_model_url(EducationExperienceList, 'changelist')},
            {'title': '服务类别', 'url': self.get_model_url(MyServiceProjectType, 'changelist')},
            {'title': '服务列表', 'url': self.get_model_url(MyServiceProjectList, 'changelist')},
            {'title': '自媒体列表', 'url': self.get_model_url(MyBlogList, 'changelist')},
            {'title': '联系我的信息', 'url': self.get_model_url(ContactMe, 'changelist')},
        )}
        return (
            MyHomePageMenu,
        )


xadmin.site.register(views.CommAdminView, GlobalSettings)  # 全局设置加载
xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册主体风格切换
