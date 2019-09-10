# class MyRangeIterator:
#     def __init__(self,value):
#         self.value=value
#         self.count=-1
#     def __next__(self):
#         if self.count>=self.value-1:
#             raise StopIteration
#         self.count+=1
#         return self.count

# class MyRange:
#     def __init__(self,number):
#         self.number=number
#     def __iter__(self):
#         item = 0
#         while item<self.number:
#             yield item
#             item += 1
#
# a=MyRange(5).__iter__()
# while True:
#     try:
#         print(a.__next__())
#     except:
#         break
# for i in MyRange(5):
#     print(i)




# def my_range(number):
#     item = 0
#     while item<number:
#         yield item
#         item += 1
# for i in my_range(5):
#     print(i)


# def my_oushu(target):
#     item=0
#     list02 = []
#     while item<len(target):
#         if target[item]%2==0:
#             list02.append(target[item])
#
#         item+=1
#     yield list02
# list01=[34,4,54,5,7,8]
# for i in my_oushu(list01):
#     print(i)


# def get_even(list_target):
#     for item in list_target:
#         if item%2==0:
#             yield item
# list01=[34,4,54,5,7,8]
# for i in get_even(list01):
#     print(i)

# list01=[34,4,54,5,7,8]
# for index,ietm in enumerate(list01):
#     print(index)

# def get_index(list_target):
#     for i in range(len(list_target)):
#         yield (i,list_target[i])
#
# for item in get_index(list01):
#     print(item)


list01=[1,2,3,4]
list02=["zs","ls","ww"]
# for i in zip(list01,list02):
#     print(i)

def zip01(*list_target):
    for i in range(len(list_target)):
        yield (list_target[i],list_target[i])
for i in zip01(list01,list02):
    print(i)