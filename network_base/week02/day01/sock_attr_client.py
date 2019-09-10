from socket import *
s=socket()
s.connect(("176.47.3.57",7777))
s.send("你好呀".encode())
data=s.recv(1024)
print(":",data.decode())
s.close()