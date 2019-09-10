from common.list_helper import ListHelper
class Skills:
    def __init__(self,name,atk,cd,speed):
        self.name=name
        self.atk=atk
        self.cd=cd
        self.speed=speed
list01=[
    Skills("横扫千军",100,0,8),
    Skills("怒气爆发",5,0,2),
    Skills("天崩地裂斩",50,2,6),
    Skills("破釜沉舟",1,3,3),
    Skills("亢龙有悔",60,4,1),
    Skills("如来神掌",110,4,1),
    Skills("如来神掌",120,4,1)
]
for item in ListHelper.find(list01,lambda item:item.name=="如来神掌"):
    print(item.name)
# list02=[]
# for item in ListHelper.find(list01,lambda item:item.atk>50):
#     list02.append(item)
# print(len(list02))

# print(ListHelper.find_count(list01,lambda item:item.cd==0))
# print(ListHelper.find_sum(list01,lambda item:item.cd))
# print(ListHelper.find_max(list01,lambda item:item.atk))
# print(ListHelper.find_min(list01,lambda item:item.atk))
# print(ListHelper.find_list(list01,lambda item:{item.name:item.atk}))
ListHelper.find_sheng(list01,lambda item:item.atk)
for i in list01:
    print(i.atk)