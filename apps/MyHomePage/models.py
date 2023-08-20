# coding:utf-8
__author__ = 'Mr.数据杨'
__explain__ = '我的个人主页模型文件'

from django.db import models
from django.utils import timezone


# 我的基本信息
class MyInformation(models.Model):
    my_info = models.CharField(
        max_length=255,
        verbose_name="我的基本信息", help_text="我的基本信息"
    )
    full_name = models.CharField(
        max_length=10,
        verbose_name="我的姓名", help_text="我的姓名"
    )
    age = models.CharField(
        max_length=2,
        verbose_name="我的年龄", help_text="我的年龄"
    )
    address = models.CharField(
        max_length=20,
        verbose_name="我的地址", help_text="我的地址"
    )
    email = models.EmailField(
        max_length=30,
        verbose_name="我的邮箱", help_text="我的邮箱"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="联系电话", help_text="联系电话"
    )
    wechart = models.CharField(
        max_length=20,
        verbose_name="我的微信", help_text="我的微信"
    )
    job = models.CharField(
        max_length=20,
        verbose_name="我的职业", help_text="我的职业"
    )
    qq = models.CharField(
        max_length=20,
        verbose_name="我的QQ", help_text="我的QQ"
    )
    # 我的技能
    skill_info = models.CharField(
        max_length=255,
        verbose_name="技能基本信息", help_text="技能基本信息"
    )
    # 我的教育&职业履历
    education_experience_info = models.CharField(
        max_length=255,
        verbose_name="教育&职业履历", help_text="教育&职业履历"
    )
    # 我的收费服务
    service_info = models.CharField(
        max_length=255,
        verbose_name="收费服务介绍", help_text="收费服务介绍"
    )
    # 我的自媒体
    site_info = models.CharField(
        max_length=255,
        verbose_name="自媒体介绍", help_text="自媒体介绍"
    )

    class Meta:
        verbose_name = '我的基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.full_name


# 我的教育信息
class EducationExperienceList(models.Model):
    EducationExperienceChoices = (
        ("0", "教育信息"),
        ("1", "职业履历")
    )
    education_experience_type = models.CharField(
        choices=EducationExperienceChoices,
        max_length=1,
        verbose_name="类别选择", help_text="数据类别选择"
    )
    name = models.CharField(
        max_length=30,
        verbose_name="学校或者企业名称", help_text="学校或者企业名称"
    )
    duration_time = models.CharField(
        max_length=13, default="yyyy - yyyy",
        verbose_name="时间信息", help_text="时间信息"
    )
    info = models.CharField(
        max_length=50,
        verbose_name="学校或者企业介绍", help_text="学校或者企业介绍"
    )

    class Meta:
        verbose_name = '我的教育&职业履历列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 我的服务信息
class MyServiceProjectType(models.Model):
    type_en = models.CharField(
        max_length=20, default='',
        verbose_name="英文类别名称", help_text="英文类别名称"
    )
    type_cn = models.CharField(
        max_length=20,
        verbose_name="中文类别名称", help_text="中文类别名称"
    )

    class Meta:
        verbose_name = '服务类别信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_cn


class MyServiceProjectList(models.Model):
    type_name = models.ForeignKey(
        MyServiceProjectType, on_delete=models.CASCADE,
        verbose_name='服务项目类别', help_text="服务项目类别"
    )
    title = models.CharField(
        max_length=30,
        verbose_name="服务名称", help_text="服务名称"
    )
    info = models.CharField(
        max_length=50,
        verbose_name="服务简介", help_text="服务简介"
    )
    img = models.ImageField(
        upload_to='MyServiceProject/', default='MyServiceProject/default.png',
        verbose_name='服务封面', help_text="若没有选择封面，则使用默认封面",
        null=True, blank=True
    )
    url = models.URLField(
        max_length=500,
        verbose_name="服务外链", help_text="服务外链"
    )

    class Meta:
        verbose_name = '我的服务明细'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 我的博客首页
class MyBlogList(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="自媒体站点名称", help_text="自媒体站点名称"
    )
    info = models.CharField(
        max_length=50,
        verbose_name="自媒体简介", help_text="自媒体简介"
    )
    img = models.ImageField(
        upload_to='MyBlog/', default='MyBlog/default.png',
        verbose_name='自媒体封面', help_text="若没有选择封面，则使用默认封面",
        null=True, blank=True
    )
    url = models.URLField(
        max_length=500,
        verbose_name="服务外链", help_text="服务外链"
    )

    class Meta:
        verbose_name = '自媒体列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 联系我的信息
class ContactMe(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="姓名", help_text="姓名"
    )
    email = models.CharField(
        max_length=50,
        verbose_name="邮箱", help_text="邮箱"
    )
    subject = models.CharField(
        max_length=50,
        verbose_name="主题", help_text="主题"
    )
    message = models.TextField(
        default="",
        verbose_name="内容", help_text="内容"
    )
    add_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="提交时间", help_text="提交时间"
    )

    class Meta:
        verbose_name = '联系我的信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject
