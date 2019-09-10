import os,time
pid=os.fork()
filename="./1.txt"
size=os.path.getsize(filename)
fr=open(filename,"rb")
def top():
    fw=open("4.txt","ab")
    n=size//2
    fw.write(fr.read(n))
    fr.close()
    fw.close()
def bot():
    # fr = open(filename, "rb")
    fw = open("4.txt", "ab")
    fr.seek(size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()
if pid>0:
    time.sleep(1)
    top() #复制上半部分文件
elif pid==0:
    time.sleep(2)
    bot() #复制下半部分文件
else:
    print("创建进程失败")