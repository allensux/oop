# coding:utf8

"""
功能名称：
作者：
创建时间：
"""
# import sys
#
# # print(dir(sys))
#
#
# print(sys.__doc__)


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)









