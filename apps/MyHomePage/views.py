# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View  # 基于类实现需要继承的view
from MyHomePage.models import *
from django.http import HttpResponse

class MyHomeIndex(View):
    # 我的基本信息
    MyInformation = MyInformation.objects.all()
    # 我的教育&职业履历
    EducationExperienceList = EducationExperienceList.objects.all()
    # 我的服务项目
    MyServiceProjectType = MyServiceProjectType.objects.all()
    MyServiceProjectList = MyServiceProjectList.objects.all()
    # 我的自媒体
    MyBlogList = MyBlogList.objects.all()
    # 联系我
    ContactMeData = ContactMe()

    def get(self, request):
        return render(request, 'HomePage/index.html', {
            'MyInformation': self.MyInformation[0],
            'MySkill': self.MyInformation[0].skill_info,
            'EducationExperience': self.MyInformation[0].education_experience_info,
            'EducationExperienceList': self.EducationExperienceList,
            'MyServiceProject': self.MyInformation[0].service_info,
            'MyServiceProjectType': self.MyServiceProjectType,
            'MyServiceProjectList': self.MyServiceProjectList,
            'MyBlog': self.MyInformation[0].site_info,
            'MyBlogList': self.MyBlogList,
        })

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')

        ContactMeData = self.ContactMeData

        ContactMeData.name = name
        ContactMeData.email = email
        ContactMeData.title = title
        ContactMeData.message = message

        ContactMeData.save()

        return HttpResponse("感谢您的提交")
