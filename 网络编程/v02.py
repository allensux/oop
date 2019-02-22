# Coding:utf8

"""
UDP:
- 客户端v02：
        - 建立socket
        - 发送消息（IP+port）到指定服务器
        - 等待服务端反馈
"""
import socket

def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = "send request"
    # 发送的数据必须是bytes格式;string换成bytes格式，使用encode()进行编码，默认是uft-8
    data = text.encode()
    print("data is",data)
    print(type(data))

    # 发送
    sock.sendto(data, ("127.0.0.1",7852))

    # 接收服务端反馈,接收的是bytes，需要进行解码decode()，默认是utf-8
    data, addr = sock.recvfrom(200)

    rec = data.decode()

    print(rec)
    print(type(rec))

if __name__ == '__main__':
    clientFunc()