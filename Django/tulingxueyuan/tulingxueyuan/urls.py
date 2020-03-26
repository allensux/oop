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

from Django.tulingxueyuan.teacher import views
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
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.index), # http://127.0.0.1:8000/index/
    url(r'^$', views.index),  # http://127.0.0.1:8000/h() 即可匹配正则表达式
    # url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',views.withparam)
    url(r'^withparam/(?P<year>[1,2][0][0,1][0-9])/(?P<month>[0][0-9]|[1][0-2])',views.withparam),
]


"""带参数 /search/page/432"""
