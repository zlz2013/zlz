from multiprocessing import Process,Value
from random import randint
import time

#创建共享内存
money=Value("i",5000)

#修改共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value+=randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.1)
        money.value-=randint(100,800)

m=Process(target=man)
g=Process(target=girl)
m.start()
g.start()
m.join()
g.join()

#获取共享内存余额
print("一月余额:",money.value)
