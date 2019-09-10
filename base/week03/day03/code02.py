# a=(4,4,5,5,565,6,7)
# iterator=a.__iter__()
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#     except:
#         break

# dict01={"张无忌":2,"赵敏":3}
# iterator01=dict01.__iter__()
# while True:
#     try:
#         item=iterator01.__next__()
#         print(item,dict01[item])
#     except:
#         break



# class SkillIterator:
#     def __init__(self,target):
#         self.target=target
#         self.index=0
#     def __next__(self):
#         if self.index>len(self.target)-1:
#             raise StopIteration
#         result=self.target[self.index]
#         self.index+=1
#         return result
class Skill:
    def __init__(self,name,shanghai):
        self.name=name
        self.shanghai=shanghai
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
class SkillManager:
    def __init__(self):
        self.list_skills=[]
    def add_skill(self,skill):
        self.list_skills.append(skill)
    def __iter__(self):
        for item in self.list_skills:
            yield item

skill01=SkillManager()
skill01.add_skill(Skill("横扫千军",100))
skill01.add_skill(Skill("破釜沉舟",80))
skill01.add_skill(Skill("杀气决",90))
for item in skill01:
    print(item.name,item.shanghai)
a=skill01.__iter__()
while True:
    try:
        item=a.__next__()
        print(item.name,item.shanghai)
    except:
        break