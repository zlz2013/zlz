"""
gevent_server   基于协程的TCP并发
扩展代码
"""

import gevent
from gevent import monkey
monkey.patch_all()  #在导入socket之前执行
from socket import *

def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()


#创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(3)

while True:
    c,addr=s.accept()
    print("Connect from",addr)
    # handle(c)#循环方案
    gevent.spawn(handle,c)#协程方案

s.close()




