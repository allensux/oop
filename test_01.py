# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

str = " random access man"

str = str.upper()

lisOfWords = str.split()
print(lisOfWords)
for word in lisOfWords:
    print(word[0], end='')