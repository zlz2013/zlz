"""
pool    进程池
"""
from multiprocessing import Pool
from time import ctime,sleep

#进程池事件
def worker(msg):
    sleep(3)
    print(msg)
    return ctime()
def fun():
    time=ctime().split()
    for i in time:
        print(i)
#创建进程池
p=Pool()
#向进程池添加执行事件
for i in range(20):
    msg="Hello %d"%i
    r=p.apply_async(func=worker,args=(msg,))

# p.apply_async(fun)
p.close()
p.join()
print(r.get())