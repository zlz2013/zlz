"""
linklist 链表程序实现
重点代码

思路分析：
    1.创建节点类，生成节点对象，包含数据和下一个节点的引用
    2.链表类，生成链表对象，可以对链表进行数据操作
"""
#节点类
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class Linklist:
    """
    建立链表模型
    进行链表操作
    """
    def __init__(self):
        """
        初始化链表，生成一个头节点，表示链表开始节点
        """
        self.head=Node(None)
    def init_list(self,list_):
        p=self.head
        for i in list_:
            p.next=Node(i)
            p=p.next
    #查看链表
    def show(self):
        p=self.head.next
        while p is not None:
            print(p.data,end=" ")
            p=p.next
        print()
    #查看链表长度
    def get_length(self):
        n=0
        p=self.head
        while p.next is not None:
            n+=1
            p=p.next
        return n
    #判断链表是否为空
    def is_empty(self):
        if self.get_length()==0:
            return True
        else:
            return False
    #清空链表
    def clear(self):
        self.head.next=None
    #尾部插入节点
    def append(self,data):
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=Node(data)
    #某个位置插入节点
    def insert(self,index,data):

        if index<0 or index>self.get_length():
            raise IndexError("index out of range")
        #定义p移动到插入位置的前一个
        p=self.head
        for i in range(index):
            p=p.next
        node = Node(data)
        node.next=p.next
        p.next=node
    #删除节点
    def delete(self,data):
        p=self.head
        while p.next and p.next.data != data:
            p=p.next
        if p.next is None:
            raise ValueError("data不在链表中")
        else:
            p.next=p.next.next
    #获取节点值
    def get_item(self,index):
        if index<0 or index >=self.get_length():
            raise IndexError("索引不在范围")
        p=self.head
        for i in range(index):
            p=p.next
        return p.next.data
    #修改节点值
    def get_updata(self,index,value):
        if index<0 or index >=self.get_length():
            raise IndexError("索引不在范围")
        p=self.head
        for i in range(index):
            p=p.next
        p.next.data=value


link=Linklist()
l=[1,2,3,4,5]
link.init_list(l)
link.show()
print(link.get_length())
link.append(6)
link.insert(0,100)
link.delete(6)

link.show()
print(link.get_item(5))
link.get_updata(3,1)
link.show()


'''abc'dd" '''
'abc"dd'

