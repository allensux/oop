# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

# L = [1,2,3,4,5]
#
# sum = 0
# # while L:
# #     sum += L[0]
# #     L= L[1:]
# #
# # print(sum)
#
#
# for i in L:
#     sum += i
# print(sum)


from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^hello$', view.hello),
]