"""
Thread  线程
"""

from threading import Thread
from time import sleep
import os

a=1
#线程函数
def music():
    for i in range(3):
        sleep(2)
        print("小苹果",os.getpid())
    global a
    print("a=",a)
    a=1000
#创建线程对象
t=Thread(target=music)
t.start()

for i in range(4):
    sleep(1)
    print("葫芦娃",os.getpid())
    print("a:",a)
t.join()
print(a)