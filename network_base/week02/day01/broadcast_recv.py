"""
1.创建UDP套接字
2.设置套接字可以接受广播
3.选择接收端口
"""

from socket import *
s=socket(AF_INET,SOCK_DGRAM)
#让套接字可以接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
s.bind(("0.0.0.0",9999))
while True:
    msg,addr=s.recvfrom(1024)
    print("收到的客户端消息：",msg.decode())
    print("客户端地址：",addr)
    s.sendto("Receive".encode(), addr)
s.close()