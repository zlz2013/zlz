from multiprocessing import Process,Array
from random import randint
import time

#创建共享内存
# shm=Array("i",[1,2,3,5,100])
# shm=Array("i",4)
shm=Array("c",b"hello")

def fun():
    for i in shm:
        print(i)
    shm[0]=b"H"
p=Process(target=fun)
p.start()
p.join()
for i in shm:
    print(i)
print(shm.value)