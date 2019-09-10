"""
线程属性说明
"""

from threading import Thread
from time import sleep

def fun():
    sleep(2)
    print("线程属性测试")

t=Thread(target=fun,name="SB")
# t.start()
# t.setName("NB")

print("线程名字:",t.getName())
print("线程生命周期:",t.is_alive())