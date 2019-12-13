"""守护线程:主线程结束了，子线程也必须结束"""

import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun,args=())
t1.setDaemon(True)  # 设置守护线程，必须在线程启动之前
# t1.daemon = True
t1.start()
# t1.join()  # 等待子线程执行完事

time.sleep(1)
print("Main thread end")  # 主线程先结束，如果没有守护线程，子线程会继续执行；如果有守护线程，主线程结束了，子线程也会结束；

