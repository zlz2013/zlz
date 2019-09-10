"""
线程互斥方法
"""
from threading import Thread,Event
from time import sleep


s=None  #用于通信
e=Event()   #创建线程event对象

def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s="天王盖地虎"
    e.set() #对e设置

t=Thread(target=杨子荣)
t.start()

print("说对口令就是自己人")
e.wait()    #阻塞等待口令说出
if s=="天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他...")

t.join()


