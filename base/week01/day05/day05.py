# dict2={(1,2,3):"urstc"}
# print(dict2)
# d = {'a': 3, 'b': 2, 'c': 1}
#
# print(sorted(d))
# x = [1, 'Two', 3, 'Four']
# a = x.sort(reverse=False)
# print(a)
# a = [('b',2), ('a',1), ('c', 1), ('d',4)]
# b=a.sort()
# print(a,b)
# L1 = [1, 2, 3]
# L2 = [L1, 4, 5]
# L3 = L2
# L4 = L3.copy()
# L1[1] = 10
# L3[1] = 40
# L4[2] = 50
# print(L1)
# print(L2)
# print(L3)
# print(L4)
# list01=list(("abc",))
# print(list01)
# l=[1,2,3]
# # l[2:]=[]
# del l[2]
# print(l)
# s=chr(ord("a"))
# print(s)
# list01=list(('aaa',))
# print(list01)
# A0=dict(zip(('a','b','b','d','e'),(1,2,3,4,5)))
# print(A0)
# A1=range(10)
# print(A1)
# A2=[i for i in A1 if i%2]
# print(A2)
# A3=[[i,i*i] for i in A1]
# print(A3)
#
# A2=[]
# for i in A1:
#     if i%2:
#         A2.append(i)
# print(A2)

# dict01={}
# list01=["周芷若","无忌","赵敏"]
# for i in list01:
#     dict01[i]=len(i)
# print(dict01)
# dict02={
#     i:len(i)
#     for i in list01
# }
# print(dict02)

# list01=["周芷若","无忌","赵敏"]
# list02=[101,102,103]
# dict01={}
# for key in range(3):
#     dict01[list01[key]]=list02[key]
# print(dict01)
#
# dict02={list01[key]:list02[key] for key in range(3)}
# print(dict02)

# for i in range(2):
# 	for j in range(3):
# 		if j == 2:
# 			break
# 		print(i, j)

# list1 = [2, 3, 8, 4, 9, 5, 6]
# list2 = [5, 6, 10, 17, 11, 2]
# L=list1+list2
# L=list(set(L))
# L.sort()
# print(L)
#
# x = [0, 1]
# i = 0
# i, x[i] = 1, 2
# print(x)


# s01 = {1, 2, 3}
# s02 = {2, 3, 4}
# print(s01 & s02)
# print(s01 | s02)
# print(s01 ^ s02)
# print(s02 - s01)
# print(s02 < s01)
# print(s02 > s01)



# list01=set()
# while True:
#     str01 = input("请输入：")
#     if str01=="esc":
#         break
#     else:
#         list01.add(str01)
#
# print(list01)

# manager={"曹操","刘备",'孙权'}
# jishu={"曹操","刘备",'张飞','关羽'}
# print("是经理也是技术员的为",manager&jishu)
# print("是经理不是技术员的为",manager-jishu)
# print("是技术员不是经理的为",jishu-manager)
# if "张飞" in manager:
#     print("张飞是经理")
# else:
#     print("张飞不是经理")
# print("经理和技术共有",len(manager|jishu),"人")
# print("身兼一职的有",manager^jishu)
# manager={"曹操","刘备",'孙权'}
# manager=frozenset(manager)
# print(manager)
# manager.add("张飞")
# print(manager)
# for r in range(3):
#     for c in range(5):
#         if c%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()

# for r in range(1,5):
#     for c in range(r):
#         print("#",end=" ")
#     print()

# list01=[3,4,45,5,7,9]
# for r in range(len(list01)-1):
#     for c in range(r+1,len(list01)):
#         if list01[r]>list01[c]:
#             list01[r],list01[c]=list01[c],list01[r]
# print(list01)
# result=False
# list01=[3,2,45,5,7,9,9]
# for r in range(len(list01)-1):
#     for c in range(r+1,len(list01)):
#         if list01[r] == list01[c]:
#             print("有重复元素,重复的元素是:%d"%list01[r])
#             result=True
#             break
#     if result:
#         break
# if not result:
#     print("没有相同元素")

# def sanjiaoxing(count,xingzhuang):
#     for r in range(count):
#         for c in range(count):
#             print(xingzhuang,end=" ")
#         print()
#
# sanjiaoxing(5,"@")

# l=[1,2,3,4,5]
# l01=l.copy()
# print(id(l))
# print(id(l01))
# a="a"
# b=a
#
# print(id(a))
# print(id(b))
# a="b"
# print(id(a))
# print(id(b))


# list01=[]
# for i in range(4):
#     list02=[]
#     while True:
#         num=input("请输入：")
#         if num =="esc":
#             break
#         list02.append(num)
#     print()
#     list01.append(list02)
# print(list01)

# list01=[]
# list02=[]
# list03=[]
# for num in range(2,101):
#     list01.append(num)
# a=False
# for r in list01:
#     for c in range(2,r):
#         if r%c==0:
#             list02.append(r)
#             a=True
#             break
#             #print("不是素数，可整除的数是:")
#         else:
#             a=False
#                 # print("是素数:")
#     if a==False:
#         list03.append(r)
#         # break
# print(list02)
# print(list03)



