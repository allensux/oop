# coding:utf-8

from django.shortcuts import render

from django.http import HttpResponse

"""视图函数--在urls中调用
    - 视图函数需要一个参数，类型应该是HttpRequest
"""
def index(request):
    return HttpResponse("Hello Wrold!!!")
    # return render(request, "index.html")

def withparam(request, year, month):
    return HttpResponse("This is a param {0}，{1}".format(year,month))