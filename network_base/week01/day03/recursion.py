# def fun(num):
#     result=1
#     for i in range(1,num+1):
#         result*=i
#     return result
#
# print(fun(5))

#求N的阶乘
def recursion(n):
    if n<1:
        return 1
    return n*recursion(n-1)
print(recursion(4))