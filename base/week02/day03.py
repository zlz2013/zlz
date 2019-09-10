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
# def get_elements(target,vect_pos,vect_dir,count):
#     result=[]
#     for i in range(count):
#         vect_pos.x+=vect_dir.x
#         vect_pos.y+=vect_dir.y
#         result


# class enemy:
#     def __init__(self,atk,hp):
#         self.set_atk(atk)
#         self.set_hp(hp)
#     def get_atk(self):
#         return self.__atk
#     def set_atk(self,value):
#         if 10<=value<=50:
#             self.__atk=value
#         else:
#             raise Exception("超出范围")
#     def get_hp(self):
#         return self.__hp
#     def set_hp(self,value):
#         if 0<=value<=100:
#             self.__hp=value
#         else:
#             raise Exception("10<hp<100")
#
# enemy01=enemy(50,10)
# print(enemy01.get_atk(),enemy01.get_hp())
# print(enemy01.__dict__)


# class enemy:
#     def __init__(self,atk,hp):
#         self.atk=atk
#         self.hp=hp
#     @property
#     def atk(self):
#         return self.__atk
#     @atk.setter
#     def atk(self,value):
#         if 10<=value<=50:
#             self.__atk=value
#         else:
#             raise Exception("超出范围")
#     @property
#     def hp(self):
#         return self.__hp
#     @hp.setter
#     def hp(self,value):
#         if 0<=value<=100:
#             self.__hp=value
#         else:
#             raise Exception("10<hp<100")
#
# enemy01=enemy(50,10)
# print(enemy01.atk,enemy01.hp)
# print(enemy01.__dict__)


# class Person:
#     def __init__(self,name):
#         self.name=name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
#     def to(self,type,str_pos):
#         print(self.name)
#         type.run(str_pos)
#
# class Car:
#     def run(self,str_pos1):
#         print("行驶到:",str_pos1)
# lz=Person("老张")
# car=Car()
# lz.to(car,"东北")

# class Person:
#     def __init__(self,name,money):
#         self.name=name
#         self.money=money
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
# class Bank:
#     def __init__(self,name,money):
#         self.name=name
#         self.money=money
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
#     @property
#     def money(self):
#         return self.__money
#     @money.setter
#     def money(self, value):
#         self.__money = value
#     def draw_money(self,person,value):
#         person.money+=value
#         self.money-=value
# xm=Person("小明",0)
# zs=Bank("招商银行",100000)
# print(xm.money)
# zs.draw_money(xm,5000)
# print(xm.money)
# print(zs.money)


# class Enemy:
#     def __init__(self,name,hp,atk):
#         self.name=name
#         self.hp=hp
#         self.atk=atk
#     def drop_blood(self,enemy,value):
#         enemy.hp-=value
#         if enemy.hp==0:
#             print("已死亡")
# class Player:
#     def __init__(self, name, hp,atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     def drop_blood(self, enemy, value):
#         enemy.hp -= value
#         if enemy.hp==0:
#             print("已死亡,游戏结束")
# enemy01=Enemy("小兵",10,10)
# enemy01.drop_blood(enemy01,10)
# print(enemy01.hp)
# palyer01=Player("小张",100,100)
# palyer01.drop_blood(palyer01,100)
# print(palyer01.hp)


class Person:
    def __init__(self,name,money=0):
        self.name=name
        self.money=money
    def teach(self,person01,person02,game):
        print("%s教%s%s"%(person01.name,person02.name,game.name))
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    def money01(self,person):
        print("%s上班赚了:%d"%(person.name,person.money))
class Games:
    def __init__(self, name):
        self.name = name

a01=Person("张无忌")
a02=Person("赵敏")
a03=Games("打篮球")
a01.teach(a01,a02,a03)
a04=Games("画眉")
a01.teach(a02,a01,a04)
a01=Person("张无忌",10000)
a01.money01(a01)
a01=Person("赵敏",5000)
a01.money01(a01)