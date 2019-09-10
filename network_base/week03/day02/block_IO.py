"""
socket 套接字非阻塞IO
如果没有客户端连接，每隔3秒填充一个日志
"""

from socket import *
from time import sleep,ctime

#打开日志文件
f=open("log.txt","a+")

#创建TCP套接字
s=socket()
s.bind(("0.0.0.0",7777))
s.listen(3)

#设置套接字为非阻塞
# s.setblocking(False)

#设置超市检测时间
s.settimeout(5)

#等待客户端连接
while True:
    print("Waiting for connect...")
    try:
        c,addr=s.accept()
    except (BlockingIOError,timeout) as e:
        #如果没有客户端连接，每隔3秒写一个日志
        f.write("%s:%s\n"%(ctime(),e))
        f.flush()
        sleep(3)

    else:
        print("Connect from",addr)
        data=c.recv(1024).decode()
        print(data)