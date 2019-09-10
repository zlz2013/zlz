"""
http    发送网页给浏览器
"""
from socket import *
#处理客户端请求
def handle(c):
    request=c.recv(4096)
    if not request:
        return
    request_line=request.splitlines()[0]
    print(request_line)
    info=request_line.decode().split(" ")[1]
    print(info)
    if info=="/":
        with open("index.html") as f:
            response="HTTP/1.1 200 OK\r\n"
            response+="Context-Type:text/html\r\n"
            response+="\r\n"
            response+=f.read()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Context-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry...</h1>"
    #发送给网页
    c.send(response.encode())
#搭建TCP网络
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8888))
s.listen(3)
while True:
    c,addr=s.accept()
    handle(c)#处理客户端请求