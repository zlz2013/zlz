# list01=[3,2,4,6,8,8,5,3]
# # for item in list01:
# #     if item %2 ==0:
# #         list01.remove(item)
# # print(list01)
# for item in range(len(list01) - 1, -1, -1):
#     if list01[item] %2 ==0:
#         # list01.remove(list01[item])
#         del list01[item]
# print(list01)


# class Car:
#     def __init__(self,brand,model,price):
#         self.brand=brand
#         self.model=model
#         self.price=price
#     def start(self):
#         print(self.brand+"型号是："+self.model+"价格是：",self.price)
#     def move(self):
#         print(self.brand+"汽车行驶")
#
# c01=Car("宝马","X5",1000000)
# c02=Car("BYD","唐",500000)
# c01.start()
# c01.move()


# class Dog:
#     def __init__(self,name,weight=50):
#         self.n=name
#         self.w=weight
#     def sitdown(self):
#         print(self.n+"hello")
# c01=Dog("泰迪",100)
# c02=c01
# c02.weight=80
# print(c01.weight)
# c01.sitdown()

# class Enemy:
#     def __init__(self,name,damage,striking_distance,hp):
#         self.n=name
#         self.d=damage
#         self.s=striking_distance
#         self.l=hp
#     def print_self(self):
#         print("%s的攻击力是%s,攻击距离是%s,生命值是%s"%(self.n,self.d,self.s,self.l))
        # list01=[name,damage,striking_distance,hp]
        # print(list01)
# list01=[]
# for i in range(3):
#     name=input("请输入敌人的姓名：")
#     damage=input("请输入敌人的攻击力：")
#     striking_distance=input("请输入敌人的攻击距离：")
#     hp=input("请输入敌人的生命值：")
#     c01=Enemy(name,damage,striking_distance,hp)
#     list01.append(c01)
#     c01.print_self()
    # print(list01)

# def find01(list_target):
#     for item in list_target:
#         if item.n=="灭霸":
#             return item
# list02=[
#         Enemy("灭霸",999,999,999),
#         Enemy("蚩尤",888,888,888),
#         Enemy("钢铁侠",777,777,777)
# ]
# re=find01(list02)
# print(re)
# re.print_self()
#
# def find02(list_target):
#     result=[]
#     for item in list_target:
#         if item.d>=500:
#             result.append(item)
#     return result
# re=find02(list02)
# for c in re:
#     c.print_self()



    
