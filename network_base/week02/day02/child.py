"""
二级子进程处理僵尸
"""
import os,time
def f1():
    for i in range(4):
        time.sleep(2)
        print("写代码")
def f2():
    for i in range(5):
        time.sleep(1)
        print("测代码")
pid=os.fork()
if pid==0:
    print("子进程",)
    p=os.fork()#二级子进程
    if p==0:
        f2()
    else:
        os._exit(0)
elif pid>0:
    os.wait()#等一级子进程退出
    print("父进程",)
    f1()
else:
    print("error")