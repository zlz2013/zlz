

from socket import *
import struct

s=socket(AF_INET,SOCK_DGRAM)
s.bind(("0.0.0.0",7777))
while True:
    msg,addr=s.recvfrom(1024)

    data=struct.unpack("i20sif",msg)
    info="%d %-10s %d %.1f"%(data[0],data[1].decode(),data[2],data[3])
    f=open("1.txt","a")
    f.write(info)
    f.write("\n")
    f.flush()
    s.sendto("已接受:".encode(),addr)