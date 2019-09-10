# list01=[]
# def score(a):
#     list01.append(a)
#     return list01
# while True:
#     try :
#         a = int(input("请输入成绩:"))
#         print(score(a))
#     except ValueError:
#         print("输入有误请重新输入")

list01 = []
while True:

    def get_score():

        while True:
            str_score=input("请输入成绩:")
            try:
                int_score=int(str_score)
            except ValueError:
                continue
            if 1<=int_score<=100:
                list01.append(int_score)
            return list01
    print(get_score())
