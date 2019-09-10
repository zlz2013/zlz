"""
进程对象属性示例
"""
from multiprocessing import Process
from time import sleep,ctime
def tm():
    for i in range(3):
        sleep(2)
        print(ctime())
p=Process(target=tm,name="SB")
p.daemon=True
p.start()
print("name:",p.name)
print("PID:",p.pid)
print("Is alive:",p.is_alive())
print(":",p.daemon)


# p.join()
