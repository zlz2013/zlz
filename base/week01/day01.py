# sex=input("请输入性别：")
# if sex=="男":
#     print("您好，先生")
# elif sex=="女":
#     print("您好，女士")
# else:
#     print("性别未知！")


# 调试：让程序中断，逐语句执行，审查程序执行过程（流程变量取值）
# 步骤：
# 1.加入断点（程序终端的行）
# 2.调试运行
# 3.逐过程执行（F8）
# 4.停止调试（Ctrl+f2）

# price=input("请输入商品单价：")
# price=float(price)
# amount=int(input("请输入数量："))
# money=float(input("请输入金额："))
# result=money-price*amount
# if result>=0:
#     print("应找回："+str(result))
# else:
#     print("金额不够！")

#练习：在控制台中获取季度，显示该季度有多少月份
#   春 1 2 3
#   夏 4 5 6
# mon=int(input("请输入月份："))
# if 1<=mon<=12:
#     if mon<=3:
#         print("春季")
#     elif mon<=6:
#         print("夏季")
#     elif mon<=9:
#         print("秋季")
#     else:
#         print("冬季")
# else:
#     print("输入有误!")


# quarter=input("请输入季度春夏秋冬：")
# if quarter=="春":
#     print("1 2 3")
# if quarter=="夏":
#     print("4 5 6")
# if quarter=="秋":
#     print("7 8 9")
# if quarter=="冬":
#     print("10 11 12")


# number_one=int(input("请输入第一个整数："))
# number_two=int(input("请输入第二个整数："))
# operator=input("+ - * /：")
# if operator=="+":
#     print(number_one+number_two)
# elif operator=="-":
#     print(number_two-number_one)
# elif operator=="*":
#     print(number_two*number_one)
# elif operator == "/":
#     print(number_two / number_one)
# else:
#     print("运算符输入错误！")


#在控制台中输入4个数字，显示最大的数字
# num_01=float(input("请输入第一个数："))
# num_02=float(input("请输入第一个数："))
# num_03=float(input("请输入第一个数："))
# num_04=float(input("请输入第一个数："))
# a=num_01
# if a<=num_02:
#     a=num_02
# if a<=num_03:
#     a=num_03
# if a<=num_04:
#     a=num_04
#
# print("最大值是：",a)

#在控制台中输入一个成绩，
# 显示优秀、良好、及格、不及格、有误
#90-100 80-90 60-80 0-60
# score=float(input("请输入成绩："))
# if 0<=score<=100:
#     if score>=90:
#         print("优秀")
#     elif score>=80:
#         print("良好")
#     elif score>=60:
#         print("及格")
#     else:
#         print("不及格")
# else:
#     print("输入有误！")



#1.在控制台中输入一个年份，如果是闰年，
#   给变量month02赋值:29，否则28
#2.在控制台中获取一个整数，
#   如果是奇数给变量state赋值：奇数，否则偶数
# state=int(input("请输入一个整数："))
# if state%2==0:
#     print("您输入的是偶数")
# else:
#     print("奇数")
# state ="奇数" if bool(state%2) else "偶数"
# print(state)
# month02=int(input("请输入一个年份："))
# result=month02%4==0 and month02%100 !=0 or month02%400==0
# month02=29 if result else 28
# print(month02)



#在控制台中获取一个开始值，一个结束值，
# 将中间的数字显示出来
# start=int(input("请输入一个开始值："))
# end=int(input("请输入一个结束值："))
# a=start
# while a<end:
#
#     print(a)
#     a += 1

# a=0.01
# b=8844.43*10*10*10
# c=0
# while a<=b:
#     a*=2
#     print(a)
#     c+=1
# print(c)
# print(b)

# import random
# random_number=random.randint(1,100)
# c=0
# print(random_number)
# while c<3:
#     a = int(input("请输入一个数："))
#     c+=1
#     if a<random_number:
#         print("小了")
#     elif a>random_number:
#         print("大了")
#     else:
#         print("恭喜你，猜对了！",c,"次")
#         break
# else:
#   print("游戏结束")


