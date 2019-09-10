"""
epoll 服务端程序
尽量掌握

思路分析：
1.创建套接字作为监控IO
2.将套接字register
3.创建查找字典，并维护（要时刻与注册的IO保持一致）
4.循环监控IO发生
5.处理发生的IO
"""

from socket import *
from select import *

#创建套接字
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(3)

#创建epoll对象关注S
p=epoll()

#创建查找字典，用于fileno查找IO对象
fdmap={s.fileno():s}

#关注s
p.register(s,EPOLLIN|EPOLLERR)

#循环监控
while True:
    events=p.poll()
    #循环遍历发生的事件
    for fd,event in events:
        #区分事件进行处理
        if fd==s.fileno():
            c,addr=fdmap[fd].accept()
            print("Connect from",addr)
            #添加新的关注IO
            p.register(c,EPOLLIN|EPOLLERR)
            print(EPOLLIN)
            print(EPOLLERR)
            fdmap[c.fileno()]=c #维护字典
        #按位与判断是EPOLLIN就绪
        elif event & EPOLLIN:
            data=fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)#取消关注
                fdmap[fd].close()
                del fdmap[fd]   #从字典中删除
                continue
            print("Receive:",data.decode())
            fdmap[fd].send(b"OK")


