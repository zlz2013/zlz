
from socket import *
import struct
ADDR=("176.47.3.57",7777)
s=socket(AF_INET,SOCK_DGRAM)

while True:
    id = int(input("id>>"))
    name = input("name>>")
    age = int(input("age>>"))
    score = float(input("score>>"))
    data=struct.pack("i20sif",id,name.encode(),age,score)
    if not data:
        break
    s.sendto(data, ADDR)
    msg, addr = s.recvfrom(1024)
    print("From server:", msg.decode())


