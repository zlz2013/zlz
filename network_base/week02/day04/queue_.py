"""
queue   消息队列
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint

#创建消息队列
q=Queue(3)

#请求进程
def request():
    for i in range(10):
        x=randint(0,100)
        y=randint(0,100)
        q.put((x,y))

#处理请求
def handle():
    while True:
        sleep(1)
        try:
            x,y=q.get(timeout=5)
        except:
            break
        else:
            print("%d+%d=%d"%(x,y,x+y))
p1=Process(target=request)
p2=Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()
