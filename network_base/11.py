# s='zygote           \
# the cell resulting from the union \
# of an ovum and a spermatozoon'
#
# import re
# s1=re.findall(r'(\S+)\s+(.*)',s)
# print(s1)


# def fun(a,b=[]):
#     b+=[a]
#     print(b)
#
# fun(1)
# fun(2)
# fun(3)

# def zhishu():
#     for i in range(2, 100):
#         for j in range(2, i):
#             if (i % j == 0):
#                 break
#         else:
#             yield i
# f=zhishu()
# for i in f:
#     print(i)
#
# def a(val,list=[]):
#     list.append(val)
#     return list
# list1=a(10)
# list2=a(123,[])
# list3=a('a')
# print('list1=%s'%list1)
# print('list2=%s'%list2)
# print('list3=%s'%list3)


# class A(object):
#     x=1
# class B(A):
#     pass
# class C(A):
#     pass
# print(A.x,B.x,C.x)
# B.x=2
# print(A.x,B.x,C.x)
# A.x=3
# print(A.x,B.x,C.x)
# C.x=4
# print(A.x,B.x,C.x)
# A.x=5
# print(A.x,B.x,C.x)


# def abc():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in abc()])
# #
#
# ab=[lambda x:i*x for i in range(4)]
# for j in ab:
#     print(j(2))

# from collections import Counter
# import re
#
# with open('a.txt', 'r', encoding='utf-8') as f:
#     txt = f.read()
# print(txt)
# c = Counter(re.split('\W+',txt))  #取出每个单词出现的个数
# print(c)
# ret = c.most_common(1)   #取出频率最高的前10个
# print(ret)


# a=1
# b=2
# a,b=b,a
# print(a,b)
#
#
# 
# list1=[2,3,8,4,9,5,6]
# list2=[11,3,4,5,6,10]
# list3=list(set(list1+list2))
# # list3.sort()
# print(list3)




# def cnt(n):
#     dic = {1: 1, 2: 2, 3: 4}
#     if n <= 3:
#         return dic[n]
#     return cnt(n-1) + cnt(n-2) + cnt(n-3)
# print(cnt(5))



# def is_different(s1,s2):
# 	list1=list(s1)
# 	list2=list(s2)
# 	if len(list1)!=len(list2):
# 		print("不是同字母异词序")
# 	else:
# 		for x in list1:
# 			if x in list2:
# 				list2.remove(x)
# 		if list2:
# 			print("不是同字母异词序")
# 		else:
# 			print("是同字母异词序")
# if __name__=="__main__":
# 	s1="assbdcff"
# 	s2="asdsbcff"
# 	is_different(s1,s2)



# import os  # 引入os
#
# def search_file(path, str):  # 传入当前的绝对路径以及指定字符串
# 	# 首先先找到当前目录下的所有文件
# 	for file in os.listdir(path):  # os.listdir(path) 是当前这个path路径下的所有文件的列表
# 		this_path = os.path.join(path, file)
# 		# print(this_path)
# 		# if os.path.isfile(this_path):  # 判断这个路径对应的是目录还是文件，是文件就走下去
# 		# 	if str in file:
# 		# 		return this_path
# 		# else:   # 不是就再次执行这个函数，递归下去
# 		# 	search_file(this_path, str)  # 递归下去
# 		if os.path.isdir(file):
# 			search_file(this_path, str)
# 		else:
# 			if str==file:
# 				return this_path
# 	# else:
#     #     return None
#
#
# def seach_f(path,str):
# 	if str in os.listdir(path):
# 		return os.path.join(path,str)
# 	else:
# 		for file in os.listdir(path):
# 			if os.path.isdir(file):
# 				this_path = os.path.join(path, file)
# 				seach_f(this_path,str)
#
# print(seach_f(os.path.abspath("."), "11.py"))
#
# # print(os.path.abspath('../'))
# print(os.listdir(os.path.abspath(".")))



# class Solution1:
# 	# array 二维列表
#     def Find(self, target, array):
# 		self.target=target
# 		self.array=array
# 		n=len(self.array)
# 		m=len(self.array[0])
# 		flag=False
# 		if (len(self.array[0]) == 0):
# 			return False
# 		if(self.target<self.array[0][0]) or (self.target>self.array[n-1][m-1]):
# 			return False
# 		for i in range(0,n):
# 			l=0
# 			r=n-1
# 			while(l<=r):
# 				mid=(l+r)//2
# 				if(self.target<array[i][mid]):
# 					r=mid-1
# 				elif(self.target>array[i][mid]):
# 					l=mid+1
# 				else:
# 					return True
# 		return False


# class Solution:
#      # array 二维列表
#      def insert2dArray(self, seq, row, col):
#          # 没有使用numpy的array
#           # array = [[0] * col] * row 这种方式是浅拷贝，不好用
#          array = [[0 for i in range(col)] for i in range(row)]
#          for i in range(row):
#              for j in range(col):
#                  array[i][j] = seq[i * row + j]
#          return array
#
#      def Find(self, target, array):
#          # 主要思路：首先选取右上角的数字，如果该数字大于target，则该列全大于target，删除该列；
#          # 如果该数字小于小于target，则该列全小于target，删除该行。
#          found = False
#          row = len(array)
#          if row:
#              col = len(array[0])
#          else:
#              col = 0
#
#          if row > 0 and col > 0:
#              # find index of top right-hand corner
#              i = 0
#              j = col - 1
#              # if never meets lower-left corner
#              while i < row and j >= 0:
#                  if array[i][j] == target:
#                      found = True
#                      # forget break
#                      break
#                  elif array[i][j] > target:
#                      j -= 1
#                  elif array[i][j] < target:
#                      i += 1
#          return found
#
# if __name__ == '__main__':
#      answer = Solution()
#      seq = [1, 2, 8, 9, 2, 4, 9, 12, 4, 7, 10, 13, 6, 8, 11, 15]
#      matrix = answer.insert2dArray(seq, 4, 4)
#      print(matrix)
#      print(answer.Find(2, matrix))


# import random
# s=random.randint(2,5)
# print(s)

# res=''
# s='The length of string is Error!'
# for i in s:
#     if i==' ':
#         res+='20%'
#     else:
#         res+=i
# print(res)

# def div1(x,y):
#     print('%s/%s=%s'%(x,y,x/y))
#
# def div2(x,y):
#     print('%s//%s=%s'%(x,y,x//y))
# div1(5,2)
# div1(5,2)
# div2(5,2)
# div2(5.,2.)


# class AA(object):
#     def __init__(self,a,b):
#         self.__a=a
#         self.__b=b
#
#     def myprint(self):
#         print('a=',self.__a,'b=',self.__b)
#
#     def __call__(self, num):
#         print('call:', num + self.__a)


# def fun1(*args):
#     def fun2(*args,func):
#         def fun3(*args):
#             # fun(*args)
#             return func
#         return fun3
#     return fun2

# a1=AA(10,20)
# a1.myprint()
# a1(80)


# alist=[3,8,2,9,13,0,5,7]
# # print(alist.sort(reverse=True))
# # print(alist)
# print(sorted(alist,reverse=True))
# print(alist)

# alist=list(range(10))
# print(alist)
# for i in alist:
#     alist.remove(i)
# print(alist)

# import json
# a={'2':'a',2:'b',"3":'c'}
# print(json.dumps(a))
# b=json.loads(json.dumps(a))
# print(b)