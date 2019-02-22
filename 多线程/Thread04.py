"""多线程执行使用threading"""

import time
import threading

def loop1(in1):
    print('Start loop1 at :', time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print('End loop1 at :', time.ctime())

def loop2(in1, in2):
    print('Start loop2 at :', time.ctime())
    print("我是参数",in1, "和参数", in2)
    time.sleep(2)
    print('End loop2 at :', time.ctime())

def main():
    print('Starting at :', time.ctime())
    # 启动多线程
    t1 = threading.Thread(target=loop1, args= ("王大鹏",))
    t1.start()# 线程启动

    t2 = threading.Thread(target=loop2, args= ("sunlimin", "damin"))
    t2.start()  # 线程启动

    t1.join() # 等待loop1执行完毕
    t2.join() # 等待loop2执行完毕
    # loop1("haha")
    # loop2("1","2")
    print('All done at :', time.ctime())

if __name__ == '__main__':
    main()