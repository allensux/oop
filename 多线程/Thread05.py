"""非守护线程:主线程结束了，但子线程仍继续执行"""

import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun,args=())
t1.start()

time.sleep(1)
print("Main thread end")

