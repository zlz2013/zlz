# class StaffManager:
#     def __init__(self):
#         self.staffs=[]
#     def add_staff(self,value):
#         self.staffs.append(value)
#     def get_staff_salary(self):
#         total_salary=0
#         for i in self.staffs:
#             total_salary+=i.Calculate()
#         return total_salary
# class Salary:
#     def __init__(self,salary):
#         self.salary=salary
#     def Calculate(self):
#         total=self.salary
#         return total
# class GeneralStaff(Salary):
#     def __init__(self,salary):
#         super().__init__(salary)
#     def Calculate(self):
#         total=self.salary
#         return total
# class Programmer(Salary):
#     def __init__(self,salary,bonus):
#         self.bonus=bonus
#         super().__init__(salary)
#     def Calculate(self):
#         total=self.salary+self.bonus
#         return total
# class Sales(Salary):
#     def __init__(self, salary, commission):
#         self.commission=commission
#         super().__init__(salary)
#     def Calculate(self):
#         total= self.salary + self.commission * 0.8
#         return total
# a01=StaffManager()
# b01=GeneralStaff(1000)
# b02=Programmer(1000,2000)
# b03=Sales(2000,10000)
# a01.add_staff(b01)
# a01.add_staff(b02)
# a01.add_staff(b03)
# print(a01.get_staff_salary())



class Student:
    def __init__(self,name="",age=0,score=0):
        self.name=name
        self.age=age
        self.score=score
    def __mul__(self, other):
        return Student(self.age*other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __imul__(self, other):
        self.age*=other
        return self
    def __lt__(self, other):

        return self.score < other
    def __str__(self):
        return "学生姓名:%s,学生年龄:%d,学生成绩:%d"%(self.name,self.age,self.score)
    def __repr__(self):
        return 'Student("%s",%d,%d)'%(self.name,self.age,self.score)
s01=Student("张三",18,99)
print(str(s01))
print(repr(s01))
print(eval(repr(s01)))
s01.name="李四"
print(str(s01))
print(eval(repr(s01)))
s01.age=s01.age*10
s01.age=0.5*s01.age
print(id(s01))
s01.age*=0.5
print(id(s01))
print(str(s01))