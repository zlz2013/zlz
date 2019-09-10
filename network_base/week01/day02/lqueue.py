"""
lqueue.py   链式队列
重点代码

思路分析：
    1.基于链表模型完成链式栈
    2.链表开端作为队头，尾端作为队尾
"""
class LQueueError(Exception):
    pass
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
#链式队列类
class LQueue:
    def __init__(self):
        #初始头尾指向一个没有实际意义的节点
        self.front=self.rear=Node(None)
    def is_empty(self):
        return self.front==self.rear
    #入队 尾动
    def enqueue(self,elem):
        self.rear.next=Node(elem)
        self.rear=self.rear.next
    #出队 头动
    def dequeue(self):
        if self.front==self.rear:
            raise LQueueError("Queue is empty")
        self.front=self.front.next
        return self.front.data

if __name__=="__main__":
    lq=LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty():
        print(lq.dequeue())