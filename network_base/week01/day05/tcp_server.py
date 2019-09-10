"""
tcp_server.py   TCP套接字服务端流程
重点代码
"""

import socket
#1.创建流式套接字
sockfd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#2.绑定地址
sockfd.bind(("0.0.0.0",8888))
#3.设置sockfd为监听套接字
sockfd.listen(3)
#4.等待处理客户端链接
while True:
    print("waiting for connect ...")
    try:
        connfd,addr=sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("Server exit...")
        break
    #5.消息收发
    while True:
        data=connfd.recv(1024)
        if not data:
            break
        print("Message",data.decode())
        n=connfd.send("**Thanks**".encode())
        print("Send %d bytes"%n)
    connfd.close()
#6.关闭套接字
sockfd.close()