from socket import *
sockfd=socket(AF_INET,SOCK_DGRAM)
ADDR=("127.0.0.1",7777)

while True:
    find=input(">>")
    if not find:
        break
    sockfd.sendto(find.encode(), ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("From server:", msg.decode())
sockfd.close()
