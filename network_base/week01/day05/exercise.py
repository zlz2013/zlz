from socket import *
s=socket()
s.bind(("0.0.0.0",8888))
s.listen(3)
c,addr=s.accept()
print("connect from",addr)

#以二进制方式写入
f=open("111.png","wb")

#循环接受内容，写入文件
while True:
    data=c.recv(1024)
    if data==b"##":
        break
    f.write(data)
data=c.recv(1024)
print(data.decode())
f.close()
c.close()
s.close()