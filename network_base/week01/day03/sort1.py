"""
基本排序算法训练
"""



#冒泡排序算法
# def bubble(list_):
#     #外层循环表达比较多少轮
#     for i in range(len(list_)-1):
#         #内层循环把控比较次数
#         for j in range(len(list_)-1-i):
#             if list_[j]>list_[j+1]:
#                 list_[j],list_[j+1]=list_[j+1],list_[j]
l=[3,1,2,6,5,8,4,7,9]
# bubble(l)
# print(l)

#选择排序算法
# def select(list_):
#     for i in range(len(list_)-1):
#         min=i
#         for j in range(i+1,len(list_)):
#             if list_[min]>list_[j]:
#                 min=j
#         if min!= i:
#             list_[i],list_[min]=list_[min],list_[i]
# select(l)
# print(l)

#插入排序算法
# def insert(list_):
#     for i in range(1,len(list_)):
#         x = list_[i]
#         j=i-1
#         while j>=0 and list_[j]>x:
#             list_[j+1]=list_[j]
#             j-=1
#         list_[j+1]=x
# insert(l)
# print(l)

#快速排序算法
def sub_sort(list_,low,high):
    #基准数
    x=list_[low]
    while low<high:
        #后面的数小于X放到前面的空位
        while list_[high]>=x and high>low:
            high-=1
        list_[low]=list_[high]#将数往前甩
        while list_[low]<x and low<high:
            low+=1
        list_[high]=list_[low]#将数往后甩
    list_[low]=x#将基准数插入
    return low
#low表示第一个数序号    high表示最后一个数序号
def quick(list_,low,high):
    if low<high:
        key=sub_sort(list_,low,high)
        quick(list_,low,key-1)
        quick(list_,key+1,high)
quick(l,0,len(l)-1)
print(l)

# def select(list_):
#     for i in range(len(list_)-1):
#         for j in range(i+1,len(list_)):
#             if list_[i]>l[j]:
#                 list_[i],list_[j]=list_[j],list_[i]
# select(l)
# print(l)