# coding:utf8

"""
功能名称：
作者：
创建时间：
"""
"""匿名函数"""

print([i + 100 for i in range(10)])

def func(x):
    return x + 100

print(list(map(func, range(10))))

print(list(map(lambda x: x + 100, range(10))))  # 匿名函数

