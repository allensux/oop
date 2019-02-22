# coding:utf8

import time

def test():

    orderId = ''
    for ID in range(1, 5):
        item1 = "<item>" + \
                "<orderID>" + str(ID) + "</orderID>" + \
                "<time>" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + "</time>" + \
                "</item>"

        orderId += item1
    messge = "<MbfBody>" + orderId + "</MbfBody> "
    print(messge)

test()