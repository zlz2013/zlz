"""
thread_class
自定义线程类演示
"""

from threading import Thread

"""
1.继承Thread
2.重写__init__和run
"""
class ThreadClass(Thread):
    def __init__(self,attr):
        self.attr=attr
        super().__init__()

    #很多方法配合完成任务
    def f1(self):
        print("步骤1")
    def f2(self):
        print("步骤2")

    def run(self):
        self.f1()
        self.f2()

t=ThreadClass("xxx")
t.start()
t.join()