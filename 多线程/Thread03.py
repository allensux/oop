"""多线程执行使用threading"""

import time
import threading

def loop1():
    print('Start loop1 at :', time.ctime())
    time.sleep(4)
    print('End loop1 at :', time.ctime())

def loop2():
    print('Start loop2 at :', time.ctime())
    time.sleep(2)
    print('End loop2 at :', time.ctime())

def main():
    print('Starting at :', time.ctime())
    # 启动多线程
    t = threading.Thread(target=loop1, args= ())
    t.start()

    t = threading.Thread(target=loop2, args= ())
    t.start()

    print('All done at :', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)