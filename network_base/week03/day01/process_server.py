"""
基于多进程的网络并发模型
重点代码


"""

from socket import *
import os,sys
import signal
from multiprocessing import Process

#创建监听套接字
Host="0.0.0.0"
Port=8888
ADDR=(Host,Port)

#处理客户端请求
def handle(c):
    while True:
        data=c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"ok")
    c.close()

s=socket()#TCP套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(3)

#处理僵尸进程
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

print("Listen the port %d..."%Port)

#循环等待客户端链接
while True:
    try:
        c,addr=s.accept()
    except KeyboardInterrupt:
        sys.exit("服务端退出")
    except Exception as e:
        print(e)
        continue

    #创建线程处理这个客户端
    t=Process(target=handle,args=(c,))
    t.daemon=True   #设置主线程退出，分支线程也退出
    t.start()

     #handle处理完客户端请求，子进程也退出
    # 无论出错或者父进程都要循环回去接受请求
    #c对于父进程没用
    c.close()