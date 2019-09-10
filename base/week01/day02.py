# month=int(input("请输入月份:"))
# year=int(input("请输入年份:"))
# if 1<month or month>12:
#     print("输入有误！")
# elif month==2:
#     if year%4==0 and year%100!=0 or year%400 ==0 :
#         print("29天")
#     else:
#         print("28天")
# elif month==4 or month==6 or month==9 or month==11:
#     print("30天")
# else:
#     print("31天")
#
# number=0
# count=0
# while number<=100:
#     count+=number
#     number+=1
# print(count)

# thickness=0.01
#
# for count in range(5):
#     thickness*=2
#     print(thickness)


# 1.累加1-100之间的数
# number=0
# for sum in range(101):
#     number+=sum
# print(number)

# number=0
# for sum in range(10,51):
#     unit=sum%10
#     if unit==2 or unit==5 or unit==9:
#         number+=sum
#     print(sum,end="+")
# print("=",number)

# import random
#
# num_1=random.randint(1,10)
# num_2=random.randint(1,10)
# result=input("请输入",num_1,"+",num_2,"=?")
# # sum=num_1+num_2
# # print(num_1,num_2,sum)
#
#
# # if count_1==sum:
# #     score=10
# # else:
#     score=5

# name ="123"
# name="123456"
# print(name)

# 练习：在控制台中获取一个字符串，打印每个字符的编码值
# str_1=input("请输入一个字符：")
# for item in str_1:
#
#     print(ord(item))
# 练习2：在控制台中重复录入一个编码值，打印字符，
#       如果没有输入编码值，而直接回车，则退出循环
# while True:
#     chr_1=input("请输入一个编码：")
#     if chr_1 == "":
#         break
#     chr_2=int(chr_1)
#     print(chr(chr_2))

# s01="请计算%d+%d=？" %(num1,num2)
# %占位符 %d:整数 %s:字符串 %f:浮点数

# print("%s的面积是:%.1f,周长是:%.2f"%("圆形",52.5,35.25))


# for second in range(120,-1,-1):
#     print("%02d:%02d"%(second//60,second%60))


# str01=input("请输入：")
# print(str01[0])
# print(str01[-1])
# if len(str01)%2==1:
#     print(str01[len(str01)//2])
# print(str01[-3::1])
# print(str01[::-1])


# value = int(input("请输入一个整数:"))
#
# print("*" * value)
# for inem in range(value-2):
#     print("*" + " " * (value - 2) + "*")
#     count += 1
# print("*" * value)

# 练习：羽毛球拍15元，球3元，水2元，有200元，每种至少一个有多少可能
# qiupai=15
# qiu=3
# water=2
# money=200
# money01=200-15-3-2
#
# n=0
# for x in range(13):
#     for y in range(61):
#         for z in range(91):
#             if qiupai * x + qiu * y + water * z == 180:
#                 n+=1
# print(n)
# 练习：有四个数字：1,2,3,4能组成多少个互不相同且无重复的三位数，各有多少？
# count=0
# for num in range(1,5):
#     for num1 in range(1,5):
#         for num2 in range(1,5):
#             if num==num1 or num==num2 or num1==num2:
#                 print(str(num)+str(num1)+str(num2))
#                 count+=1
#
# print(count)

# count=0
# num=100
# num1=100
# while num/2>=0.01:
#     count+=1
#     num/=2
#     num1+=num*2
#
#
#     print(round(num1,2),end="+")
#     print("距离是：%.2f"%num1)
# print()
# print(count)

# 练习：假设有一个池塘，里面有无线的水，现在有两个空水壶，
#   分别位5升和6升，问题是如果只用这两个水壶从池塘里取得3升的水

# shuibei1 = 5
# shuibei2 = 6
# count1=0
# for count in range(3):
#
#     count1=shuibei2-shuibei1
#     shuibei1=shuibei1-1
# print(shuibei1)

