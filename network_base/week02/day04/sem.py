"""
sem 信号量
"""
from multiprocessing import Semaphore,Process
from time import sleep
import os

#创建信号量 最多允许三个任务执行
sem=Semaphore(3)

#任务函数
def handle():
    sem.acquire()#想执行必须消耗一个信号量
    print("%d 执行任务"%os.getpid())
    sleep(2)
    print("%d 执行任务完毕" % os.getpid())
    sem.release()#增加信号量

#10人想执行
for i in range(10):
    p=Process(target=handle)
    p.start()
    #p.join()
