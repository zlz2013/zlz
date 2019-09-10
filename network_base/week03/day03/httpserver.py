"""
http server 2.0
IO多路复用 http练习

思路分析：
1.使用类进行封装
2.从用户使用角度决定类的编写
"""

from socket import *
from select import select



#功能类 具体http server功能
class HTTPServer:
    def __init__(self,host,port,dir):
        self.address=(host,port)
        self.host=host
        self.port=port
        self.dir=dir
        self.create_socket()
        self.bind()
        self.rlist=[]
        self.wlist=[]
        self.xlist=[]

    #创建套接字
    def create_socket(self):
        self.s=socket()
        self.s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    def bind(self):
        self.s.bind(self.address)

    #具体处理请求
    def handle(self,r):
        #接收http 请求
        request=r.recv(4096)
        # print(request)
        #防止客户端断开
        if not request:
            self.rlist.remove(r)
            r.close()
            return
        #提取请求内容
        request_line=request.splitlines()[0]
        print(request_line)
        info=request_line.decode().split(" ")[1]
        print(r.getpeername(),":",info)

        #info 分为访问网页或者其他内容
        if info =="/" or info[-5:]==".html":
            self.get_html(r,info)
        else:
            self.get_data(r,info)

    def get_data(self,r,info):
        response = "HTTP/1.1 200 Not Found\r\n"
        response += "Context-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Waiting httpserver 3.0...</h1>"
        r.send(response.encode())
    #处理网页请求
    def get_html(self,r,info):

        if info == "/":
            filename=self.dir+"/index.html"
        else:
            filename=self.dir+info
        try:
            fd=open(filename)
        except Exception:
            #没有网页
            response="HTTP/1.1 404 Not Found\r\n"
            response += "Context-Type:text/html\r\n"
            response += "\r\n"
            response += "<h1>Sorry...</h1>"
        else:
            #存在网页
            response = "HTTP/1.1 200 OK\r\n"
            response += "Context-Type:text/html\r\n"
            response += "\r\n"
            response += fd.read()

        r.send(response.encode())

    #启动服务
    def serve_forver(self):
        self.s.listen(3)
        print("Listen the port",self.port)
        self.rlist.append(self.s)

        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.s:
                    c,addr=r.accept()
                    print("Connect from",addr)
                    self.rlist.append(c)
                else:
                    #处理请求
                    self.handle(r)

if __name__=="__main__":
    #希望通过http server类快速搭建http服务，
    #用以展示自己的网页

    #用户自己决定内容
    HOST="0.0.0.0"
    PORT=8000
    DIR="./static"  #网页存放位置

    httpd=HTTPServer(HOST,PORT,DIR)  #实例化对象
    httpd.serve_forver()   #启动http服务
