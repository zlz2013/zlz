# def fun01():
#     print("fun01执行了")
# a=fun01
# a()


class Skills:
    def __init__(self,name,atk,cd,speed):
        self.name=name
        self.atk=atk
        self.cd=cd
        self.speed=speed
list01=[
    Skills("横扫千军",100,0,8),
    Skills("怒气爆发",5,1,2),
    Skills("天崩地裂斩",50,2,6),
    Skills("破釜沉舟",1,3,3),
    Skills("亢龙有悔",60,4,1)
]
# def find01(list_target):
#     for i in list_target:
#         if i.cd==0:
#             yield i
# def find02(list_target):
#     for i in list_target:
#         if i.atk>10:
#             yield i
# def find03(list_target):
#     for i in list_target:
#         if i.speed<5:
#             yield i
def con01(i):
    return i.cd==0
def con02(i):
    return i.atk>10
def con03(i):
    return i.speed<5
def find(list_target,con):
    for i in list_target:
        if con(i):
            yield i
list02=[1,2,3,4,5,6,7]
for i in find(list02,lambda item:item%2==0):
    print(i)
    # print("技能:%s,速度:%d,攻击力:%d,CD:%d"%(i.name,i.speed,i.atk,i.cd))
