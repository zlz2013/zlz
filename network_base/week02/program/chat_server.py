"""
chat room
env:python3.5
socket udp fork 练习
"""

from socket import *
import os,sys
#服务器地址
ADDR=("0.0.0.0",7777)

#存储用户,{name:addr}
user={}

#登录
def do_login(s,name,addr):
    if name in user or "管理员" in name:
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b"ok",addr)

    #通知其他人
    msg="\n欢迎%s进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户插入字典
    user[name]=addr
#转发消息
def do_chat(s,name,text):
    msg="\n%s : %s"%(name,text)
    for i in user:
        if i!=name:
            s.sendto(msg.encode(),user[i])
#退出
def do_quit(s,name):
    msg="\n%s 退出了聊天室"%name
    for i in user:
        if i !=name:
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b"EXIT",user[i])
    del user[name]

#循环接收客户端请求
def do_request(s):
    while True:
        data,addr=s.recvfrom(1024)
        tmp=data.decode().split(" ")#拆分请求
        #根据请求类型执行不同内容
        if tmp[0]=="L":
            do_login(s,tmp[1],addr)#完成具体服务端登录工作
        elif tmp[0]=="C":
            text=" ".join(tmp[2:])#拼接消息内容
            do_chat(s,tmp[1],text)
        elif tmp[0]=="Q":
            if tmp[1] not in user:
                s.sendto(b"EXIT",addr)
                continue
            do_quit(s,tmp[1])
#搭建UDP网络
def main():
    #Udp套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid=os.fork()
    if pid<0:
        return
    elif pid==0:
        while True:
            msg=input("管理员消息:")
            msg="C 管理员消息:"+msg
            s.sendto(msg.encode(),ADDR)

    else:
    #请求处理函数
        do_request(s)

#测试代码
if __name__=="__main__":
    main()