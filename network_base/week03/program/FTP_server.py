"""
ftp 文件服务器
多线程并发/线程练习
"""

from socket import *
from threading import Thread
import os,time

#全局变量
Host="0.0.0.0"
Port=8888
ADDR=(Host,Port)
FTP="/home/tarena/桌面/FTP/"  #文件库目录

#创建文件服务器服务端功能类
class FTPServer(Thread):
    def __init__(self,client):
        self.client=client
        super().__init__()

    def do_list(self):
        #获取文件列表
        files=os.listdir(FTP)
        print(files)
        if not files:
            self.client.send("文件列表为空".encode())
        else:
            self.client.send(b"OK")
            time.sleep(0.1)

        #拼接文件列表
        files_=""
        for file in files:
            if file[0]!="." and os.path.isfile(FTP+file):
                print(file)
                files_+=file+"\n"
        self.client.send(files_.encode())

    def do_get(self,filename):
        try:
            fd=open(FTP+filename,"rb")
        except Exception:
            self.client.send("文件不存在".encode())
            return
        else:
            self.client.send(b"OK")
            time.sleep(0.1)
        while True:
            data=fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.client.send(b"##")
                break
            self.client.send(data)

    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.client.send("该文件已存在".encode())
            return
        self.client.send(b"OK")
        fd=open(FTP+filename,"wb")
        while True:
            data=self.client.recv(1024)
            if data==b"##":
                break
            fd.write(data)
        fd.close()

    #循环接受客户端请求
    def run(self):
        while True:
            data=self.client.recv(1024).decode()
            if data=="Q" or not data:
                return
            elif data=="L":
                self.do_list()
            elif data[0]=="G":
                filename=data.split(" ")[-1]
                self.do_get(filename)
            elif data[0]=="P":
                filename=data.split(" ")[-1]

                self.do_put(filename)


#网络搭建
def main():
    #创建套接字
    s=socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)
    print("Listen the port %d..."%Port)

    while True:
        try:
            c,addr=s.accept()
            print("Connect from:",addr)
        except KeyboardInterrupt:
            print("服务器程序退出")
            return
        except Exception as e:
            print(e)
            continue

        client=FTPServer(c)
        client.setDaemon(True)
        client.start()

if __name__=="__main__":
    main()