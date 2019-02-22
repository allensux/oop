# Coding:utf8

"""
UDP:
    - 服务端v01：
        - 建立socket,socket是负责具体通信的一个实例
        - 获取本机地址和端口，绑定IP和端口
        - 接收访问(接受对方发送内容)
        - 给对方反馈，此步骤为非必须步骤
"""

import socket

def serverFunc():
    # 1. 建立socket

    # socket.AF_INET:使用Ipv4协议
    # socket.SOCK_DGRAM:使用UDP协议
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 2.绑定ip和port
    # 127.0.0.1代表机器本身ip地址
    # port：7852随机指定的端口号
    # 地址是一个tuple类型(ip，port)
    addrserver = ("127.0.0.1",7852)
    sock.bind(addrserver)

    # 3. 接收对方的访问
    # 一直等待
    # recvform接受的返回值是一个元组，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    # rst = sock.recvfrom(500)
    data, addrclient = sock.recvfrom(500) # 元组写成这种形式，直接返回元组中的两个值
    print("data is:",data)
    print("type is:",type(data))

    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # 默认参数utf-8
    text = data.decode()
    print("text is:", text)
    print("text type is：" , type(text))

    # 给对方反馈的消息
    rsp = "接收请求"

    # 发送数据需要编码成bytes格式
    # 默认是utf-8
    data = rsp.encode('utf-8')
    # 向客户端发送编码后的数据data
    sock.sendto(data,addrclient)

if __name__ == '__main__':
    print("starting server...")
    serverFunc()
    print("Ending server...")
