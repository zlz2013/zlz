"""
pipe    管道通信
"""
from multiprocessing import Pipe,Process
import os,time

#创建管道对象
fd1,fd2=Pipe(duplex=True)


def read():
    while True:
        data=fd2.recv()#从管道获取消息
        print(data)
def write():
    while True:
        time.sleep(2)
        data = time.ctime()
        fd1.send(data)#向管道发送内容
r=Process(target=read)
w=Process(target=write)
r.start()
w.start()
r.join()
w.join()






