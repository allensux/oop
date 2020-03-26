# coding:utf8

"""
功能名称：
作者：
创建时间：
"""

s = '2017-11-27'
import re
print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', s))


import re
ip ='192.168.1.1'
trueIp =re.search(r'(([01]?\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',ip)
print(trueIp)