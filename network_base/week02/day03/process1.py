"""
multiprocessing  示例1
"""
import multiprocessing as mp
from time import *

a=1
def fun():
    print("开始一个新的进程")
    sleep(5)
    global a
    print("a:",a)
    a=1111
    print("子进程结束了")
#创建进程对象
p=mp.Process(target=fun)
p.start()#启动进程

sleep(2)
print("父进程干点啥")
p.join(1)#回收进程
print("a::",a)