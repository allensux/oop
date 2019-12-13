# coding:utf8

"""
功能名称：
作者：
创建时间：
"""
from threading import Timer


def printHello():
    print("Hello World")
    t = Timer(2, printHello)
    t.start()


printHello()