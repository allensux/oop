# coding:utf8

"""
功能名称：
作者：
创建时间：
"""
#
# seq = ['one', 'two', 'three']
# # seq = 'sam'
# for i, element in enumerate(seq):
#     print(i, element)

# seq = ['one', 'two', 'three']
# # seq = 'sam'
# for (i, element) in enumerate(seq):
#     print(i, element)

# 迭代
# L = [1, 2, 3]
# I = iter(L)
# print(I.__next__())
# print(I.__next__())
# print(next(I))

# key = ['a', 'b', 'c']
# value = [1, 2, 3]
# print('内置函数：',dict(zip(key, value)))
# D = {}
# for k, v in zip(key, value):
#     D[k] = v
# print(D)



# 字典迭代

D = {'a': 1, 'b': 2, 'c': 3}
I = iter(D)
for key in I:
    print(key, D[key])
# print(next(I))
# print(I.__next__())
# for key in D.keys():
#     print(key)

L1 = ['import', 'print(sys.path)\n', 'x = 2\n']
L = [line.strip() for line in L1]
print(L)


def hah():
    ...


x = 5//2
print(x)
