# coding:utf-8
"""tulingxueyuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
urls这是主路由
"""

from django.conf.urls import include, url
from Django.tulingxueyuan.teacher import views, teacher_url

# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
##################################
# from django.urls import path
#
# urlpatterns = [
#
#     path('index/', views.index),
# ]

###############################
"""如果是 Django >= 2.0 的版本，path() 函数无法匹配正则表达式，需要使用 re_pat
django.conf.urls下的url模块函数返回re_path"""


#############################

# 带参数
urlpatterns = [
    # url(r'^index/$', views.index), # http://127.0.0.1:8000/index/
    # url(r'^$', views.index),  # http://127.0.0.1:8000/h() 即可匹配正则表达式
    # # url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',views.withparam)
    # url(r'^withparam/(?P<year>[1,2][0][0,1][0-9])/(?P<month>[0][0-9]|[1][0-2])',views.withparam),

    # 凡是由teacher模块处理的视图的url都以teacher开头 http://127.0.0.1:8000/teacher/liudana/
    url(r'^teacher/', include(teacher_url)),

    # 嵌套参数-捕获参数的一部分   ?：表名忽略此参数 http://127.0.0.1:8000/book/page-12/
    url(r'^book/(?:page-(?P<page_number>\d+)/$)', views.do_param2),

    # 额外参数 ，使用字典表示 http://127.0.0.1:8000/yourname/
    url(r'^yourname/$', views.extremParam, {"name": "liudana"}),

    # 反向解析,直接修改  http://127.0.0.1:8000/mayiknowyourname/
    url(r'^mayiknowyourname/$', views.revParse, name = 'askname'),
]



