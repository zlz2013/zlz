"""
bitree.py   二叉树的实现

思路分析：
    1.使用链式存储，节点类设计上由两个属性变量指向引用左孩子和右孩子
    2.操作类完成二叉树的遍历
"""
from squeue import *
#二叉树节点
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

#二叉树的操作类
class Bitree:
    def __init__(self,root=None):
       self.root=root
    #先序遍历
    def preoder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preoder(node.left)
        self.preoder(node.right)
    #中序遍历
    def inoder(self,node):
        if node is None:
            return
        self.inoder(node.left)
        print(node.data,end=" ")
        self.inoder(node.right)

    # 后序遍历
    def outoder(self, node):
        if node is None:
            return
        self.outoder(node.left)
        self.outoder(node.right)
        print(node.data, end=" ")
    #层次遍历
    def leveloder(self,node):
        sq = SQueue()
        sq.enqueue(node)
        while not sq.is_empty():
            node=sq.dequeue()
            print(node.data,end=" ")
            if node.left:
                sq.enqueue(node.left)
            if node.right:
                sq.enqueue(node.right)

if __name__=="__main__":
    #后续遍历树  BFGDIHECA
    #构建树
    b=TreeNode("B")
    f=TreeNode("F")
    g=TreeNode("G")
    d=TreeNode("D",f,g)
    i=TreeNode("I")
    h=TreeNode("H")
    e=TreeNode("E",i,h)
    c=TreeNode("C",d,e)
    a=TreeNode("A",b,c)



    bt=Bitree(a)
    bt.preoder(bt.root)
    print()
    bt.inoder(bt.root)
    print()
    bt.outoder(bt.root)
    print()
    bt.leveloder(bt.root)
