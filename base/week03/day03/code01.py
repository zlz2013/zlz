class Wife:
    def __init__(self,weight):
        self.weight=weight

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,value):
        if 50<value<60:
            self.__weight=value
        else:
            raise WeightError(value,"超出范围","self.__weight=value")
class WeightError(Exception):
    def __init__(self,value,str_msg,code):
        super().__init__()
        self.weight_value=value
        self.msg=str_msg
        self.code=code
try:
    w01=Wife(65)
except WeightError as abc:
    print("错误提示:",abc.msg)
    print("错误数值:",abc.weight_value)
    print("错误代码:",abc.code)