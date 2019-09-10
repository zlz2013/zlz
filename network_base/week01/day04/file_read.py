"""
file_read.py    文件读取演示
"""

#打开文件
fd=open("tetst","r")
# fd=open("timg.jpeg","rb")
#循环读取文件
# while True:
#     data=fd.readline()
#     #读到文件结尾得到空字符串，此时跳出循环
#     if not data:
#         break
#     print("读取的内容",data,end="")
data=fd.readlines()
print(data)
for i in fd:
    print(i,end="")