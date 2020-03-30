# coding:utf-8


from django.conf.urls import include
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
# 带参数
urlpatterns = [
    url(r'^liudana/$', views.do_app), # http://127.0.0.1:8000/teacher/liudana/

]



