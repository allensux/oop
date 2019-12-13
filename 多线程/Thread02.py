"""多线程执行"""
import time
import _thread as thread # 有问题

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
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print('All done at :', time.ctime())

if __name__ == '__main__':
    main()