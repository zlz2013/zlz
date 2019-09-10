import time


def get_time(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time() - start
        print(end)
        return result
    return wrapper

class Student:
    
    @get_time
    def study(self):
        print("学习")
        time.sleep(2)

    @get_time
    @get_time
    def play(self):
        print('玩耍')
        time.sleep(3)
stu=Student()
stu.play()
