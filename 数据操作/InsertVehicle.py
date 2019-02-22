# coding:utf8
"""循环插入大东铁西车辆"""

import requests

for i in range(1,11):
    m = str(i).zfill(6) # 字符串，补齐6位，不够前面补0
    vin = "LBVKY91DECO" + m # 拼接字符串
    # vin = "LBVCZ11LMNO" + m
    # print(vin)
    url = 'http://10.10.171.247:7090/rest/testSap/{0}/BMW0000AAHEV'.format(vin)
    requests.get(url)