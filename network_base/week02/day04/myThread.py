"""
练习：线程类
"""

from threading import Thread
from time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs={}):

        super().__init__()
        self.target=target
        self.args=args
        self.kwargs=kwargs

    def run(self):
        self.target(*self.args,**self.kwargs)



def player1():
    print("ni hao ")

def player(sec,song):
    for i in range(3):
        print("playing %s : %s"%(song,ctime()))
        sleep(sec)
t=MyThread(target=player1)
t1=MyThread(target=player,args=(2,),kwargs={"song":"凉凉"})

t.start()
t1.start()
t.join()
t1.join()

