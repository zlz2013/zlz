# def fun01():
#     print("fun01执行咯")
#     return 1
#
# result=fun01()
# print(result)

# def add(num1,num2):
#     result=num1+num2
#     return result
# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# re = add(a,b)
# print("结果是：",re)

# def seconds(num1,num2,num3):
#     result=num1*3600+num2*60+num3
#     return result
# hour=int(input("请输入小时："))
# min=int(input("请输入分钟："))
# second=int(input("请输入秒："))
# re=seconds(hour,min,second)
# print("结果是：",re)


# def seconds(num1,num2,num3):
#     return num1*3600+num2*60+num3
#
# print("结果是：",seconds(int(input("请输入小时：")),int(input("请输入分钟：")),int(input("请输入秒："))))


# def scores(score):
#     if 0<=score<=100:
#         if score>=90:
#             return "优秀"
#         elif score>=80:
#             return "良好"
#         elif score>=60:
#             return "及格"
#         else:
#             return "不及格"
#     else:
#         return "输入有误！"
# print(scores(float(input("请输入成绩："))))

# def is_leap_year(year):
#     """
#     判断是否是闰年
#     :param year: 是闰年返回True，
#     :return:
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# def get_day(month,year):
#     if 1>month or month>12:
#         return "输入有误！"
#     if month==2:
#         # if is_leap_year(year):
#         #     return 29
#         # return 28
#         return 29 if is_leap_year(year) else 28
#     if month in (4,6,9,11):
#         return 30
#     return 31
# # print(get_day(int(input("请输入月份:")),int(input("请输入年份:"))))
# print(get_day(2,2000))


# def get_sushu(begin,end):
#     list03=[]
#     for r in range(begin,end):
#         for c in range(2,r):
#             if r%c==0:
#                 break
#                 #print("不是素数，可整除的数是:")
#         else:
#             list03.append(r)
#             # break
#     return list03
# print(get_sushu(2,10))

# def is_prise(count):
#     if count<2:
#         return False
#     for item in range(2,count):
#         if count%item==0:
#             return  False
#     return True
# def number_range(begin,end):
#     list01=[r for r in range(begin,end) if is_prise(r)]
#     # for r in range(begin,end):
#     #     if is_prise(r):
#     #         list01.append(r)
#     return list01
#
# print(number_range(2,30))

# def fun02(p1):
#     p1[0]=300
# num02=[100,200]
# fun02(num02)
# print(num02)


# list01=[3,4,45,5,7,9]
# for r in range(len(list01)-1):
#     for c in range(r+1,len(list01)):
#         if list01[r]>list01[c]:
#             list01[r],list01[c]=list01[c],list01[r]
# print(list01)

# def sort01(list_target):
#     for r in range(len(list_target) - 1):
#         for c in range(r + 1, len(list_target)):
#             if list_target[r] > list_target[c]:
#                 list_target[r], list_target[c] = list_target[c], list_target[r]
#
#
# list01 = [3, 4, 45, 5, 7, 9]
# sort01(list01)
# print(list01)

# count=0
# def num01():
#     global count
#     count+=1
#
# num01()
# print(count)
# num01()
# print(count)
# num01()
# print(count)

# def fun01(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# list01=(1,2,3,7)
# # fun01(*list01)
# # fun01(a=1,b=2,c=3,d=5)
# # fun01(d=1,b=2,c=3,a=5)
# # fun01(1,b=2,c=3,d=5)
# # fun01(a=1,b=2,3,5)#错误
# # fun01(1,2,c=3,d=5)
# dict01={"d":2,"b":3,"c":4,"a":5}
# fun01(**dict01)

# def fun01(a,b,c,d=0):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# fun01(b=2,a=100,c=[1,2,3])


# def seconds(num1=0,num2=0,num3=0):
#     return num1*3600+num2*60+num3
# print(seconds(num1=1,num2=1))


# def fun01(a,b,c):
#     pass
# def fun02(*a):
#     print(a)
# fun02("abc","qwe","dads")

# def fun01(*args):
#     sum01=0
#     for item in args:
#         sum01+=item
#     return sum01
# print(fun01(1,2,3))

# def fun01(**args,a,b,c):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
# # fun01(1,5,8,7,5,6,a=1,b=2,c=3)
# def fun01(**kwargs):
#
#     print(kwargs)
# fun01(a=1,b=2,c=3)


