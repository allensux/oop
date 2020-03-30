# coding:utf-8
"""tulingxueyuan_views URL Configuration

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
from Django.tulingxueyuan_views.teacher_app import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),


    url(r'^teacher/',views.teacher),

    url(r'^v2_exception/',views.v2_exception), # 引发Http404异常

    # 在east/urls中添加如下内容
    url(r'^v10_1', views.v10_1),
    url(r'^v10_2', views.v10_2),
    url(r'^v11', views.v11, name="v11"),

    # Get示例
    url(r'^v8/', views.v8_get),

    # Post示例
    url(r'^v9_get/', views.v9_get),
    url(r'^v9_post/', views.v9_post),

    url(r'^render_test/', views.render_test),

    # 替换模板中的值，传参
    url(r'^render2_test/', views.render2_test),

    url(r'^render3_test/', views.render3_test),

    url(r'^render4_test/', views.render4_test),

    url(r'^get404/', views.get404),
]
