"""
file_read.py    文件写入演示
"""

f=open("test","ab+")
f.write("抠脚大汉\n\n".encode())
f.write("213\n".encode())

f.writelines(["abc\n".encode(),"哎呀，死鬼".encode()])

f.close()
