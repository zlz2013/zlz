"""
squeue.py  队列的顺序存储
重点代码
思路分析：
    1.基于列表完成存储结构
    2.通过封装规定队头和队尾操作
"""
#自定义异常类
class SQueueError(Exception):
    pass
#队列操作类
class SQueue:
    def __init__(self):
        self._elems=[]
    #判断队列空
    def is_empty(self):
        return self._elems==[]
    #入队
    def enqueue(self,elem):
        self._elems.append(elem)
    #出队
    def dequeue(self):
        if not self._elems:
            raise SQueueError("Queue is empty")
        return self._elems.pop(0)
if __name__=="__main__":
    sq=SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    sq.enqueue(40)
    while not sq.is_empty():
        print(sq.dequeue())