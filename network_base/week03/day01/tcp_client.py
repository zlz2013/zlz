"""
tcp_client.py   TCP套接字客户端流程
重点代码
"""
from socket import *
#创建套接字
sockfd=socket()#参数默认即TCP套接字
#请求链接服务端
server_addr=("176.47.3.57",8888)
sockfd.connect(server_addr)
#消息发收
while True:
    data=input("Msg>>:")
    if not data:
        break
    sockfd.send(data.encode())#转换成字节串
    data=sockfd.recv(1024)
    print("Server:",data.decode())
#关闭套接字
sockfd.close()

