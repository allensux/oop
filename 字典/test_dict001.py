# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

import pprint
# myCat = {'name':'xiaocao', 'age': 12, 'size':'44kg'}
#
# print(myCat.items())
# for k in myCat.values():
#     print(k,end='')

message = """BOOKS and doors are the same thing.
you open them, and you go through into another world."""

words = message.split()
print(words)

count = {}

for word in words:
    # print(word[0])
    count.setdefault(word, 0)  # 每个键值出现的次数
    count[word] += 1
pprint.pprint(count)