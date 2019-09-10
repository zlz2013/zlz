"""
UDP 套接字客户端
重点代码
"""
from socket import *
#创建套接字
sockfd=socket(AF_INET)
#服务端地址
ADDR=("176.47.3.57",7777)

#循环发送消息
while True:
    data=input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr=sockfd.recvfrom(1024)
    print("From server:",msg.decode())
#关闭套接字
sockfd.close()


