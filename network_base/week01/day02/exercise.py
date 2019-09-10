from lstack import *


ls=LStack()
while True:
    exp=input("请输入：")
    tmp=exp.split(' ')
    for i in tmp:
        if i not in ['+','-','p']:
            ls.push(float(i))
        elif i =='+':
            x=ls.pop()
            y=ls.pop()
            ls.push(y+x)
        elif i=='-':
            x = ls.pop()
            y = ls.pop()
            ls.push(y - x)
        elif i=='p':
            print(ls.top())


