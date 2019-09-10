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

res=list(map(lambda e:(e.name,e.cd),list01))
print(res)
# for i in sorted(list01,key=lambda e:e.atk,reverse=True):
#     print(i.atk)

re01=list(filter(lambda e:50<e.atk<=100,list01))
print(re01[0].name)
for i in re01:
    print(i.name)
# re=max(list01,key=lambda e:e.atk)
# print(re.atk)
re=min(list01,key=lambda e:e.speed)
print(re.name)

i=max(list01,key=lambda e:len(e.name))
print(i.name)

