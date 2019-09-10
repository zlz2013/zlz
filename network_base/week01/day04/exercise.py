
import os

a=input("请输入文件路径:")

# path=os.listdir(a)
# print(path)
# b=a.split("/")[-1]
# print(b)
if os.path.exists(a):
    f=open(a,"rb")
    fd = open("1904", "wb")
    for i in f:
        fd.write(i)
else:
    print("没有找到该文件")

try:
    fr=open(a,"rb")
except  FileNotFoundError as e:
    print(e)
else:
    fw=open("1905","wb")
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()
