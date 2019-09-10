# string = 'abcdef'
# def string_reverse2(string):
#     t = list(string)
#     l = len(t)
#     for i,j in zip(range(l-1, 0, -1), range(l//2)):
#         t[i], t[j] = t[j], t[i]
#     return "".join(t)
# print(string_reverse2(string))


#
# a=[1,2,4]
# b=[1,5,6]
# c=set(a)
# d=set(b)
# print(list(c^d))
# # c=a.extend(b)
# # print(c)
#
# # print(a)
# # d='dfdg'
# # a.extend(d)
# # print(a)
# import json
# f='[2, 4, 5, 6]'
# print(json.loads(f))
# print(eval(f))


import os
# for i,j,k in os.walk("./"):
#     print(k)
# def getFiles(dir, suffix):
#
#     res = []
#     for root, dirs, files in os.walk(dir):
#         # print(root)
#         # print(dirs)
#         # print(files)
#         for filename in files:
#             # print(filename)
#             name, suf = os.path.splitext(filename)
#             # print(name)
#             print(suf)
#             if suf == suffix:
#                 res.append(os.path.join(root, filename))
#
#     # print(res)
#
# getFiles("./", '.pyc')

# a=os.path.splitext("111.py")
# print(a)



# print(100//3)   #33
# print(100**3)   #100万
# print(100%3)    #1
# print(100>>1)    #25
# print(100>>2)    #25
# print(100 >> 3)   #12
# print(100 >> 4)   #12
# print(100 or 3)
# print(101 & 55)
# print(101 | 55)
#
# a=range(10)
# b=range(20)
# z=zip(a,b)
# print(list(z))
# print(len(list(z)))
# print(len(list(z)))


import threading
import time
def _wait():
    time.sleep(60)
t1=time.time()
t=threading.Thread(target=_wait,daemon=True)
t.start()
t2=time.time()
print(t2-t1)