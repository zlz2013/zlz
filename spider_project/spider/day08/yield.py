# def fun1():
#     for i in range(2):
#         yield i
#
# g=fun1()
# # print(g.__next__())
# # print(g.__next__())
# while True:
#     try:
#         print(g.__next__())
#     except:
#         break


#用Python实现range
class myrange():
    def __init__(self,start,stop=None,step=None):
        if stop is None:
            self.start=0
            self.stop=start-1
        else:
            self.start=start
            self.stop=stop
        self.step=step


