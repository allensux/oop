# Coding:utf8

"""
功能名称：
作者：
创建时间：
"""

import re
s = """
    hello csvt
    csvt hello
    hello csvt hello
    csvt hehe
    """
r = r"^csvt"
print(s)
f = re.findall(r, s, re.M)
print(f)