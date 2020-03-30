# coding:utf-8
import string

import request
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from django.template import loader
from django.views import defaults

"""视图返回
符合http协议要求的任何内容，包括json，string，html等
"""

def teacher(r):
    return HttpResponse("这是teacher的一个视图")


def v2_exception(r):
    raise Http404
    # return HttpResponse("OK")

"""重定向 302"""
def v10_1(r):
    return HttpResponseRedirect("/V11")

def v10_2(r):
    return HttpResponseRedirect("V11")

def v11(r):
    return HttpResponseRedirect("这是V11的访问返回")

"""GET"""
def v8_get(request):
    rst = ""
    for k,v in request.GET.items():
        rst += k + "-->" + v
        rst += ","
        new_rst = rst.strip(",")
    # new_rst = rst.strip(string.punctuation)

    return HttpResponse("Get Value Request is {}".format(new_rst))


"""POST"""
def v9_get(request):
    # 渲染模板并返回
    """render是render_to_response的升级版"""
    # return render_to_response("for_post.html")
    return render(request,"for_post.html")

def v9_post(request):
    rst = ""
    for k, v in request.POST.items():
        rst += k + "-->" + v
        rst += ","
        newrst = rst.strip(",")

    return HttpResponse("{}".format(newrst))


def render_test(request):
    # 环境变量
    # c = dict()
    rst = render(request, 'render.html')
    # rst = HttpResponse(request, "render.html")  不好用？
    return rst

def render2_test(request):
    # 环境变量 传参数到模板
    C = dict()
    C["name"] = "sunlimin"

    rst = render(request, 'render2.html', context=C)
    return rst

def render3_test(request):

    # 得到模板
    t = loader.get_template("render3.html")  # 返回template的一个实例
    print(type(t))
    rst = t.render({"name": "render3"})
    print(type(rst))
    return HttpResponse(rst)  # 视图返回的必须是Response子类，不能是其他的类

#  render_to_response用法
def render4_test(request):
    # 加载模板 render2.html
    rsp = render_to_response("render2.html", context={"name":"haha"})
    return rsp

# 使用系统内建函数返回404异常
def get404(request):
    return defaults.page_not_found(request, Exception, template_name='404.html')
    # return defaults.server_error(request, Exception)
