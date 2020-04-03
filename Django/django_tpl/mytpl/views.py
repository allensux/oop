# coding:utf-8
from django.shortcuts import render

# Create your views here.


def one(request):
    rst = render(request, 'one.html')
    return rst

def two(request):
    # C = dict()
    # C["name"] = "sunlimin"

    rst = render(request, 'two.html', context={"name":"sunlimin", "name2":"sunlimin2"})
    return rst


def three(request):
    C = dict()
    C["score"] = [20,60,77,88,90]

    rst = render(request, 'three.html', context=C)  # 传入上下文context
    return rst


def four(request):
    C = dict()
    C["name"] = "王晓静"

    rst = render(request, 'four.html', context=C)  # 传入上下文context
    return rst


def five_get(request):
    return render(request, "five_get.html")


def five_post(request):
    print(request.POST)
    return render(request, "one.html")