# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

def pack():
    list = []
    for i in range(1, 7):
        m = str(i).zfill(6)  # 字符串，补齐6位，不够前面补0
        code = 'BMWIPM000PACK0000000BMW00' + m
        # print(code)
        list.append(code)
    print(list)
pack()