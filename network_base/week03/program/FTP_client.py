"""
FTP 客户端
"""
from socket import *
import sys,time

ADDR=("176.47.3.57",8888)

#客户端处理类
class FTPClient:
    def __init__(self,sock):
        self.sock=sock

    #获取文件列表
    def do_list(self):
        self.sock.send(b"L")   #发送请求
        #等待回复
        data=self.sock.recv(1024).decode()
        if data=="OK":
            #一次接受文件列表字符串
            data=self.sock.recv(4096)
            print(data.decode())
        else:
            print(data)

    #下载文件
    def do_get(self,filename):
        #发送请求
        self.sock.send(("G "+filename).encode())
        #等待回复
        data=self.sock.recv(128).decode()
        if data=="OK":
            fd=open(filename,"wb")
            #接受文件
            while True:
                data=self.sock.recv(1024)
                if data==b"##":
                    break
                fd.write(data)
            fd.close()
        else:
            print(data)

    #上传文件
    def do_put(self,filename):
        try:
            fd=open(filename,"rb")
        except Exception:
            print("文件不存在")
            return
        self.sock.send(("P " + filename.split("/")[-1]).encode())
        # 等待回复
        data = self.sock.recv(128).decode()
        if data=="OK":
            while True:
                data=fd.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sock.send(b"##")
                    break
                self.sock.send(data)
            fd.close()
        else:
            print(data)
    def do_quit(self):
        self.sock.send(b"Q")
        self.sock.close()
        sys.exit("谢谢使用")

#创建客户端网络
def main():
    s=socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp=FTPClient(s) #实例对象
    #循环发送请求
    while True:
        print("\n=======命令选项=======")
        print("****     list     ****")
        print("****   get file   ****")
        print("****   put file   ****")
        print("****     quit     ****")
        print("=======命令选项=======")

        cmd=input("输入命令:")
        if cmd.strip()=="list":
            ftp.do_list()
        elif cmd[:3]=="get":
            filename=cmd.strip().split(" ")[-1]
            ftp.do_get(filename)
        elif cmd[:3]=="put":
            filename=cmd.strip().split(" ")[-1]
            print(filename)

            ftp.do_put(filename)

        elif cmd.strip()=="quit":
            ftp.do_quit()

        else:
            print("请输入正确命令")

        # s.send(cmd.encode())


if __name__=="__main__":
    main()