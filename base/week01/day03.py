# list01=[1,"大强",True]
# list02=list(list01)
# list02=list(range(5))
# print(list01)
# print(list02)
# list01.append("苏")
# print(list01)
# list01.insert(0,"唐僧")
# print(list01)
# list01.remove(1)
# print(list01)
# del list01[2]
# print(list01)


# 练习：1.在控制台中录入所有学生成绩
#     请输入学生总数
#     请录入第一个学生成绩
#     2.获取总分 最高分 最低分
# students=int(input("请输入学生总数："))
# list1=[]
# for item in range(students):
#     score = int(input("请输入第%d个学生的成绩："%(item+1)))
#     list1.append(score)
# print(list1)
# result0=sum(list1)
# result1=max(list1)
# result2=min(list1)
# print("总成绩为：%d,最大;值为：%d，最小值为：%d"%(result0,result1,result2))

# import copy
# list01=["张无忌",["赵敏","周芷若"]]
# list02=copy.deepcopy(list01)
# list01[1][1]="老张"
# print(list01)
# print(list02)
#
# num=input("请输入四位数：")
# sum01=int(num[0])+int(num[1])+int(num[2])+int(num[3])
# print(sum01)

# score=input("请输入学生的姓名")
# list01=[]
# while True:
#     name=input("请输入学生姓名：")
#     if name=="esc":
#         break
#     if name in list01:
#         continue
#     list01.append(name)
# print(list01)
# for item in range(len(list01)-1,-1,-1):
#     print(list01[item])


# lisr_score=[]
# while True:
#     score=int(input("请输入学生的成绩："))
#     if score>=60:
#         lisr_score.append(score)
#     if score==0:
#         break
# print(lisr_score)
# print("最大值为：%d"%max(lisr_score))

# list_score=[60,85,100,26,20,90]
# list01=[]
# for item in list_score:
#     if item>60:
#         list01.append(item)
# print(list01)
# max_value=list_score[0]
# for i in range(1,len(list_score)):
#     if max_value < list_score[i]:
#         max_value=list_score[i]
# print(max_value)

# list01=[]

# while True:
#     str_value=input("请输入:")
#     if str_value=="esc":
#         break
#     list01.append(str_value)
# print(list01)
# str_result="***".join(list01)
# print(str_result)

# 练习：英文单词反转 how are you->you are how
# str_value="how are you"
# list01=str_value.split(" ")
# print(list01)
# list01=list01[::-1]
# print(list01)
# str_value=" ".join(list01)
# print(str_value)

#
# list01=[56,36,68,44,868]
# list02=[]
# for item in list01:
#     list02.append(item%10)
# print(list02)
# list03=[item%10 for item in list01]
# print(list03)

# list01=[]
# while True:
#     num01=(input("请输入："))
#     if num01=="esc":
#         break
#     list01.append(int(num01))
#     min_value = list01[0]
#     for item in range(1,len(list01)):
#         if min_value>=list01[item]:
#             min_value=list01[item]
#     print("最小值为：",min_value)
# print(list01)
# print("最小值为：%d"%min(list01))
#
import random
list01=[]
while True:
    red=random.randint(1,33)
    if red in list01:
        continue
    if len(list01)==7:
        break
    list01.append(red)
print(list01)
blue=random.randint(1,17)
list01.append(blue)
print(list01)


list02=[]
count=1
while True:
    if len(list02)==7:
        break
    red = int(input("请输入第%d个红色球号码：" % count))
    if red >33 or red <0:
        print("号码不在范围内！")
        continue
    elif red in list02:
        print("号码已经重复，请重新输入！")
        continue
    count+=1
    list02.append(red)
print(list02)
blue=int(input("请输入蓝色球号码："))
list02.append(blue)
print(list02)

if list01==list02:
    print("恭喜你，中奖了！")

