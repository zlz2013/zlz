"""
dict 服务端

功能：业务逻辑处理
模型：多进程TCP并发
"""

from multiprocessing import Process
from socket import *
import signal,sys,time
from operation_db import *

#全局变量
ADDR=('0.0.0.0',8000)

#数据库对象
db=Database()

#注册处理
def do_register(c,data):
    tmp=data.split(' ')
    name=tmp[1]
    passwd=tmp[2]
    if db.register(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')

#登录处理
def do_login(c,data):
    tmp=data.split(' ')
    name=tmp[1]
    passwd=tmp[2]
    if db.login(name,passwd):
        c.send(b'OK')
    else:
        c.send(b'Fail')

#查单词
def do_query(c,data):
    tmp=data.split(' ')
    name=tmp[1]
    word=tmp[2]
    db.insert_history(name,word)#插入历史记录
    #找到返回解释，没找到返回none
    mean=db.query(word)
    if not mean:
        c.send("没有找到该单词".encode())
    else:
        msg="%s : %s"%(word,mean)
        c.send(msg.encode())

#查历史记录
def do_hist(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    r=db.history(name)
    if not r:
        c.send(b'Fail')
        return
    c.send(b'OK')
    for i in r:
        #i-->(name,word,time)
        # print(i)
        msg="%s  %-16s  %s"%i
        print(msg)
        time.sleep(0.1)
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b"##")

#循环接受客户端请求,分配处理函数
def request(c):
    db.create_cursor()#生成游标
    while True:
        data=c.recv(1024).decode()
        print(c.getpeername(),':',data)
        if not data or data=='E':
            sys.exit()
        elif data[0]=="R":
            do_register(c,data)
        elif data[0]=="L":
            do_login(c,data)
        elif data[0]=="W":
            do_query(c,data)
        elif data[0]=="H":
            do_hist(c,data)




#搭建网络
def main():
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    #循环等待客户端连接
    print("Listen the port 8000")
    while True:
        try:
            c,addr=s.accept()
            print("connect from",addr)
        except KeyboardInterrupt:
            s.close()
            db.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue

        #为客户端创建子进程
        p=Process(target=request,args=(c,))
        p.daemon=True
        p.start()

if __name__=='__main__':
    main()
