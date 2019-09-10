"""
chat room
客户端
"""
from socket import *
import os,sys

#服务端地址
ADDR=("176.47.3.42",8888)

#发送消息
def send_msg(s,name):
    while True:
        try:
            text=input("发言:")
        except KeyboardInterrupt:
            text="quit"
        if text.strip()=="quit":
            msg='Q '+name
            s.sendto(msg.encode(),ADDR)
            sys.exit("\n%s退出聊天室"%name)
        msg="C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

#接收消息
def recv_msg(s):
    while True:
        try:
            data,addr=s.recvfrom(1024)
        except KeyboardInterrupt:
            sys.exit()
        if data.decode()=="EXIT":
            sys.exit()
        print(data.decode()+"\n发言:",end="")

#启动客户端
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    while True:
        name=input("请输入姓名:")
        msg="L "+name
        s.sendto(msg.encode(),ADDR)
        #等待反馈
        data,addr=s.recvfrom(1024)
        if data.decode()=="OK":
            print("欢迎%s进入聊天室"%name)
            break
        else:
            print(data.decode())

    #创建新进程
    pid=os.fork()
    if pid<0:
        sys.exit("error")
    elif pid==0:
        send_msg(s,name)
    else:
        recv_msg(s)
#测试代码
if __name__=="__main__":
    main()

