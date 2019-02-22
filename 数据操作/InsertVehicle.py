# coding:utf8
"""循环插入大东铁西车辆"""

import requests

for i in range(1,7):
    m = str(i).zfill(6) # 字符串，补齐5位，不够前面补0
    #vin = "LBVKY91WASGL" + m # 拼接字符串
    vin = "LBVKY910418" + m
    # print(vin)
    url = 'http://10.10.171.247:7090/sap/save/?vin={0}&homologationModel=BMW0000AAHEV( 2d)'.format(vin)
    requests.get(url)