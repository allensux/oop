"""多线程属性示例"""

import time
import threading

def loop1():
    print("start loop1 at : ", time.ctime())
    time.sleep(4)
    print("End loop 1 at:", time.ctime())

def loop2():
    print("start loop2 at :", time.ctime())
    time.sleep(2)
    print("End loop2 at :", time.ctime())

def loop3():
    print("start loop3 at :", time.ctime())
    time.sleep(5)
    print("End loop3 at :", time.ctime())


def main():
    print("Starting at:", time.ctime())
    t1 = threading.Thread(target=loop1, args=())
    t1.setName("线程1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName("线程2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName("线程3")
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
    time.sleep(3)

    for thr in threading.enumerate():
        print("正在运行的线程名字是： {0}".format((thr.getName())))
    print("正在运行的线程{0}".format(threading.enumerate()))
    print("正在运行的线程数量{0}".format(threading.active_count()))
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()