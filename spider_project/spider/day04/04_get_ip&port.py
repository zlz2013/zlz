import random


def get_ip():
    with open('ip_port.txt','r') as f:
        res=f.readlines()
    ip_port=random.choice(res)
    print(res)
    print(ip_port[:-1])

get_ip()