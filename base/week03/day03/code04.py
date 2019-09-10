class EmployeeManager:
    def __init__(self):
        self.emp_list=[]
    def add_emp(self,value):
        self.emp_list.append(value)
    def __iter__(self):
        for item in self.emp_list:
            yield item
class Employee:
    def __init__(self,name):
        self.name=name

emp01=EmployeeManager()
emp01.add_emp(Employee("zs"))
emp01.add_emp(Employee("ls"))
a=emp01.__iter__()
while True:
    try:
        b=a.__next__()
        print(b.name)
    except:
        break

