# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

import random
numlist = []
for i in range(5):
    numlist.append(random.randint(1,9))


# numlist.reverse()
# print(numlist)

# numlist.sort(reverse=True)
# numlist.sort()
# numlist.insert(4, 10)
# numlist.pop(2)
# print(numlist)
# s_list = sorted(numlist, reverse=True)
# print(s_list)
# print(sorted(numlist))
#
# print(numlist)

# PI = 3.14
#
# tup =(1,2,4,2,4)
# print(tup)
# print(max(tup))
# s_tup = sorted(tup) #只能通过你日志函数sorted排序
# print(s_tup)
#
#
# """python的内置函数"""
#
# l = ['a', 'b', 'c', 'd', 'e','f']
# print(l)
#
#
# print(l[:-1])
# print(l[1:])

#打印列表
# zipped = zip(l[:-1],l[1:])
# print(list(zipped))
# a = [1,2,3]
# b = [4,5,6]
# print(list(zip(a,b)))
# print(list(zip(*zip(a,b))))
# a1, a2 = zip(*zip(a,b))
# print(a1)
# print(a2)

"""产生列表"""
# nList = [i for i in range(10)]
# nList1 = [i*2 for i in range(10)]
# print(nList)
# print(nList1)
#
# pList = [pow(i, 2) for i in nList]  # pow计算2次方
# print(pList)

"""列表里的元素是列表-二位列表"""

# listOfValue = [[pow(i, 2), pow(i, 3), pow(i, 4)] for i in nList]
# print(listOfValue)

listTable = [[0]*10 for i in range(10)]
print()
print(listTable)

for i in range(1, 10):
    for j in range(1, 10):
        listTable[i][j] = i * j
# for i in range(10):
#     for j in range(10):
        print(listTable[i][j], end= ',')
    print()