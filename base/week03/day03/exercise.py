class Students:
    def __init__(self,name,age,sex,score):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=score
class Iterator:
    def __init__(self,list_target):
        self.list_target=list_target
    def iterator(self):
        for i in self.list_target:
            yield i

# def iterator(list_target):
#     for i in list_target:
#         if i.sex=="女":
#             yield i
#
# def iterator1(list_target):
#     for i in list_target:
#         if i.age>30:
#             yield i
# def iterator2(list_target):
#     for i in list_target:
#         if i.score<60:
#             yield i
list01=[]
ste01=Students("张三",60,"男",100)
ste02=Students("李四",20,"女",50)
ste03=Students("王五",50,"女",40)
list01.append(ste01)
list01.append(ste02)
list01.append(ste03)
# print("性别为女的所有同学姓名！")
# for i in Iterator(list01).iterator():
#     if i.sex == "女":
#         print(i.name)
# print("年龄大于30的所有同学姓名！")
# for i in Iterator(list01).iterator():
#     if i.age>30:
#         print(i.name)
# print("成绩小于60的所有同学姓名！")
# result=list(Iterator(list01).iterator())
# print(result[2].name)
# for i in result:
#     if i.score<60:
#         print(i.name)

a=(i.name for i in list01 if i.score<60)
for i in a:
    print(i)