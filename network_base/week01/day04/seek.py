"""
seek.py 文件偏移量
"""
#文件偏移量在开头
f=open("test","wb+")
f.write("hello world\n".encode())
f.close()
f=open("test","rb+")
print(f.tell())
f.seek(-5,2)#以开头为基准，向后移动0字节
print(f.read())