# class ICBC:
#     total_money=0
#     @classmethod
#     def print_total_money(cls):
#         print("总共创建了%d个实例对象。"%cls.total_money)
#     def __init__(self,name,money):
#         self.n=name
#         self.m=money
#         ICBC.total_money+=1
# coun01=ICBC("上海",10000)
# coun02=ICBC("静安",100000)
# coun03=ICBC("闸北",1000000)
# coun04=ICBC("普陀",10000000)
# coun05=ICBC("普陀",100000000)
# ICBC.print_total_money()


# class Vertor02:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     @staticmethod
#     def get_right():
#         return Vertor02(0,1)
#
#     @staticmethod
#     def get_up():
#         return Vertor02(-1, 0)
#
#     @staticmethod
#     def get_left():
#         return Vertor02(0,-1)
#
#     @staticmethod
#     def get_down():
#         return Vertor02(1, 0)
#
#     @staticmethod
#     def cycle_right(pos01):
#         for i in range(n):
#             change=Vertor02.get_right()
#             pos02=Vertor02(pos01.x+change.x,pos01.y+change.y)
#             pos01=pos02
#             print(pos02.x,pos02.y)
#
#     @staticmethod
#     def cycle_left(pos01):
#         for i in range(n):
#             change = Vertor02.get_left()
#             pos02 = Vertor02(pos01.x + change.x, pos01.y + change.y)
#             pos01 = pos02
#             print(pos02.x, pos02.y)
#
#     @staticmethod
#     def cycle_up(pos01):
#         for i in range(n):
#             change = Vertor02.get_up()
#             pos02 = Vertor02(pos01.x + change.x, pos01.y + change.y)
#             pos01 = pos02
#             print(pos02.x, pos02.y)
#
#     @staticmethod
#     def cycle_down(pos01):
#         for i in range(n):
#             change = Vertor02.get_down()
#             pos02 = Vertor02(pos01.x + change.x, pos01.y + change.y)
#             pos01 = pos02
#             print(pos02.x, pos02.y)
# pos01=Vertor02(2,1)
# n=int(input("请输入移动的个数:"))
# deriction=input("请输入移动的方向:")
# if deriction=="up":
#     Vertor02.cycle_up(pos01)
# if deriction=="down":
#     Vertor02.cycle_down(pos01)
# if deriction=="right":
#     Vertor02.cycle_right(pos01)
# if deriction=="left":
#     Vertor02.cycle_left(pos01)


class Student:
    def __init__(self,name,sex,score):
        self.name=name
        self.sex=sex
        self.score=score
    def print_self(self):
        print("%s的性别是:%s,成绩是:%s"%(self.name,self.sex,self.score))
    @staticmethod#姓名为张无忌的对象
    def find(list_target):
        for item in list_target:
            if item.name=="张无忌":
                return item
    @staticmethod#成绩大于60且性别是女的对象
    def find_score(list_target):
        result=[]
        for item in list_target:
            if item.sex=="女" and item.score>60:
                result.append(item)
        return result

    @staticmethod#成绩大于60的所有对象
    def find_score01(list_target):
        result = []
        for item in list_target:
            if item.score >=60:
                result.append(item)
        return result
    @staticmethod#成绩最大值
    def max_score(list_target):
        result=[]
        for i in list_target:
            result.append(i.score)
        return result
    @staticmethod#成绩最大值的对象
    def max_score01(list_target):
        for i in list_target:
            if max(Student.max_score(list_target))==i.score:
                return i
    @staticmethod#删除成绩低于60的对象
    def dele(list_target):
        for i in range(len(list_target)-1,-1,-1):
            if list_target[i].score<60:
                list_target.remove(list_target[i])
        return list_target


list02 = [
         Student("张无忌","男",99),
         Student("蚩尤","男",88),
         Student("钢铁侠","男",77),
         Student("周芷若","女",66),
         Student("赵敏","女",55),
         Student("小芳","女",44)
 ]

re=Student.find(list02)
re.print_self()
re01=Student.find_score(list02)
for i in re01:
    i.print_self()
re02=Student.find_score01(list02)
for i in re02:
    i.print_self()
re03=Student.max_score01(list02)
re03.print_self()
re04=Student.dele(list02)
for i in list02:
    i.print_self()