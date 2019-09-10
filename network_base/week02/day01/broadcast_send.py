#发送广播

from socket import *
import time

#设置广播地址
dest=("176.47.3.255",5555)
s=socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data="""
**********
小伙子很酷
**********
"""
while True:
    # data=input("Msg>>")
    time.sleep(2)
    s.sendto(data.encode(),dest)
    msg, addr = s.recvfrom(1024)
    print("From server:", msg.decode())
s.close()