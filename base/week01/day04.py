
# list01=list("abc")
# list01.append("张三")
# list01.insert(3,"李四")
# print(id(list01))
# list01[-1]="王五","a",1,2,3,5,4,6,7,10
# print(id(list01))
# list01.append("张三")
# print(list01)
# tuple01=tuple(list01)
# print(tuple01)
# t03="a"
# print(type(t03))

# month=int(input("请输入月："))
# day=int(input("请输入日："))
# day_tuple=(31,28,31,30,31,30,31,31,30,31,30,31)
# sum01=0
# for item in range(1,month+1):
#     if item<1 or item>12:
#         print("输入错误")
#     else:
#         print(day_tuple[item-1])
#     sum01+= day_tuple[item-1]
#     #print(sum)
# print(sum01+day)

# month=int(input("请输入月："))
# day=int(input("请输入日："))
# day_tuple=(31,28,31,30,31,30,31,31,30,31,30,31)
# sum_1=[]
# for item in range(1,month+1):
#     if month<1 or month>12:
#         print("输入错误")
#     else:
#         print(day_tuple[item-1])
#     sum_1.append(day_tuple[item-1])
# sum_2=sum(sum_1)
# print(sum_2+day)




# a = [('b',2), ('a',1), ('c', 1), ('d',4)]
# b = a.sort()
# print("float,%10.5f,has"%3.1415926)

# dict01={"zc":65,"mz":90,"yl":80,}
# print(dict01)
#
# for key in dict01.values():
#     print(key)

# season=input("请输入季度：")
# dict01={
#     "春季":"1 2 3",
#     "夏季":"4 5 6",
#     "秋季":"7 8 9",
#     "冬季":"10 11 12"
# }
# if season in dict01:
#     print(dict01[season])
# else:
#     print("输入有误!")
# for key,value in dict01.items():
#     if season==key:
#         print(value)
#     else:
#         print("输入的不是季度！")
#         break

# a=[1,2,4,3,5]
# # a.sort(reverse=True)
# print(sorted(a))
# print(a)

# list01=[]
# dict01={}
# while True:
#     names=input("姓名：")
#     if names=="esc":
#         break
#     list01.append(names)
#     sex=input("性别：")
#     list01.append(sex)
#     score=input("成绩：")
#     list01.append(score)
#     age=input("年龄：")
#     list01.append(age)
# print(list01)

# dict01={}
# while True:
#     names=input("姓名：")
#     if names=="esc":
#         break
#     sex=input("性别：")
#     score=int(input("成绩："))
#     age=int(input("年龄："))
#     dict01[names]=[sex,score,age]
# for key,value in dict01.items():
#     print("%s的性别是%s，成绩是%d，年龄是%d"%(key,value[0],value[1],value[2]))


# dict01={}
# while True:
#     names=input("姓名:")
#     if names=="esc":
#         break
#     list01 = []
#     dict01[names]=list01
#     while True:
#         fair = input("喜好:")
#         if fair=="esc":
#             break
#         list01.append(fair)
# print(dict01)
# for key,value in dict01.items():
#     print("%s的喜好是:%s"%(key,value))


# 将1970年到2050年中的闰年，存入列表．
# list01=[]
# for item in range(1970,2051):
#     if item %4==0 and item  %100!=0 or item%400==0:
#         list01.append(item)
# print(list01)
#
# # (1)存储多个商品信息,在控制台中显示出来.
# #    屠龙刀,10000元
# #    倚天剑,10000元
# #    打狗棒,5000元
# dict01={"屠龙刀":10000,"倚天剑":10000,"打狗棒":5000}
# print(dict01)

import random
tuple01=("石头","剪刀","布")
tuple02=("石头剪刀")
tuple03=("剪刀布")
tuple04=("布石头")
while True:
    num = random.randint(0,2)
    print(tuple01[num])
    num01=input("请输入：（石头,剪刀,布）")
    if tuple01[num]==num01:
        print("平局")
    elif tuple01[num]+num01==tuple02 or tuple01[num]+num01==tuple03 or tuple01[num]+num01==tuple04:
        print("失败")
    else:
        print("胜利")

