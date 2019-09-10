"""
基于fork的进场创建演示
"""
import os,time
print("=====")
a=1
pid=os.fork()
print(pid)
if pid<0:
    print("创建进程失败")
elif pid==0:
    os._exit(0)
    time.sleep(3)
    print("新进程")
    print("a=",a)
else:
    time.sleep(5)
    print("老进程")
    print("a=", a)
    a=11111
print("fork测试结束")
print("aaa",a)