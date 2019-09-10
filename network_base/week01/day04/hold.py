"""
空洞文件
"""
# f=open("test","wb")
# f.write(b"start")
# f.seek(1000,2)
# f.write(b"end")
# f.close()


import os
# a=os.path.getsize("dict.txt")
a="/home/tarena/桌面/zlz/第二阶段/file/day1.txt"
print(os.listdir(a))
# print(os.path.exists("test"))
# print(os.path.isfile("seek.py"))
# print(os.remove("test"))