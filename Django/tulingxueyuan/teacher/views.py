# coding:utf-8

from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse

"""视图函数--在urls中调用
    - 视图函数需要一个参数，类型应该是HttpRequest
"""
def index(request):
    return HttpResponse("Hello Wrold!!!")
    # return render(request, "index.html")

def withparam(request, year, month):
    return HttpResponse("This is a param {0}，{1}".format(year,month))

def do_app(request):
    return HttpResponse("这是个子路由!!!")
    # return render(request, "index.html")

def do_param2(r, page_number):
    return HttpResponse("Page number is {}".format(page_number))

def extremParam(r, name):
    return  HttpResponse("My name is {}".format(name))

def revParse(r):
    return HttpResponse("Your request URL is {}".format(reverse('askname')))