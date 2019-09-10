import re

port=input("端口：")
f=open("1.txt")

#找到port所在段
while True:
    data=""
    for i in f:
        if i!="\n":
            data+=i
        else:
            break
    if not data:
        break
    print(">>>",data)

    result=re.match(port,data)
    if result:
        # pattern=r"\w{4}\.\w{4}\.\w{4}"
        pattern=r"(\d{1,3}\.){3}\d{1,3}/\d+|Unknow"
        try:
            addr=re.search(pattern,data).group()
            print(addr)
        except:
            print("NO address")
        break