"""
buffer  缓冲区
"""
f=open("test","a",1)
while True:
    a=input(":")
    f.write(a)
    f.write("\n")

    # f.flush()#将缓冲内容写入磁盘
f.close()