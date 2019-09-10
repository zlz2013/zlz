from socket import *
from day01.find_dict import *




sockfd=socket(AF_INET,SOCK_DGRAM)
sockfd.bind(("127.0.0.1",7777))

while True:
    data,addr=sockfd.recvfrom(1024)
    # print("收到的单词：",data.decode())
    mean=dict(data.decode())
    sockfd.sendto(mean.encode(),addr)

