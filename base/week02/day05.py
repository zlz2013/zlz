# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def call(self):
#         print("叫")
# class Dog(Animal):
#     def __init__(self,nickname,name,age):
#         self.nickname=nickname
#         super().__init__(name,age)
#     def proter(self):
#         print(self.nickname,self.name,self.age,"看守")
# class Bird(Animal):
#     def fly(self):
#         print("飞")
# dog01=Dog("儿子","二哈",18)
# dog01.proter()
# print(isinstance(Dog,Animal))
# print(isinstance(dog01,Animal))
# print(isinstance(dog01,Dog))
# print(issubclass(Dog,Animal))
# print(issubclass(Animal,Animal))
# print(issubclass(Bird,Animal))
# print(issubclass(Bird,Animal))



# class Car:
#     def __init__(self,brand,model,price):
#         self.barnd=brand
#         self.model=model
#         self.price=price
#
# class ElectricCar(Car):
#     def __init__(self,battery_capacity,charging_power,brand,model,price):
#         self.battery_capacity=battery_capacity
#         self.charging_power=charging_power
#         super().__init__(brand,model,price)
# ele01=ElectricCar(100,100,"BMW","x5",20000)
# print(ele01.__dict__)



# class Weaposn:
#     def __init__(self,name):
#         self.name=name
#     def damage(self,type,Person):
#         type.hp(Person)
#         print(self.name,"爆炸了")
# class Person:
#     def hp(self,person):
#         print(person,"受伤了")
#
#
# a=Weaposn("手雷")
# person=Person()
# a.damage(person,"小兵")


# def f1(fn):
#     def f2():
#         print("aaaa")
#         fn()
#     return f2
# def f3():
#     print("bbbb")
# # print(f1(5))
# # f1(5)
# a=f1(f3)
# a()



class GraphicsManager:
    def s(self,value,r=0,a=0):
        if not isinstance(value,Graphics):
            raise TypeError()
        value.area(r,a)
class Graphics:
    def area(self,r=0,a=0):
        raise NotImplementedError
class Circular(Graphics):
    def area(self,r=0,a=0):
        s=3.14*r**2
        print(s)
class Asquare(Graphics):
    def area(self,r=0,a=0):
        s=r**2
        print(s)
class Asquare1(Graphics):
    def area(self,r=0,a=0):
        s=r*a
        print(s)
s01=Circular()
s02=GraphicsManager()
s02.s(s01,10)
s03=Asquare1()
s02.s(s03,5,4)
