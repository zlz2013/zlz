def error(str_number):
    while True:
        try:
            number = int(input(str_number))
            return number
        except:
            print("输入有误,请重新输入！")