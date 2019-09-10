"""
套接字属性演示
"""

from socket import *
#创建套接字
s=socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("176.47.3.57",7777))
s.listen(3)
c,addr=s.accept()
print("客户端地址为:",addr)
c.recv(1024)
c.send("感谢你的链接".encode())
print("地址类型",s.family)
print("地址类型",s.type)
print("绑定的地址",s.getsockname())
print("文件描述符",s.fileno())
print("客户端地址:",c.getpeername())
#设置套接字端口立即重用

