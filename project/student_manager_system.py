class StudentMode:
    def __init__(self,name="",age=0,score=0,id=0):
        self.id=id
        self.name=name
        self.age=age
        self.score=score
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id=value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

class StudentMangerController:
    def __init__(self):
        self.stu_list=[]

    def stu_list(self):
        return self.stu_list
    def add_stu(self,stu_manege):
        stu_manege.id=self.generate_id()
        self.stu_list.append(stu_manege)
    def generate_id(self):
        return self.stu_list[-1].id + 1 if len(self.stu_list) > 0 else 1
    def remove_stu(self,id):
        for item in self.stu_list:
            if item.id==id:
                self.stu_list.remove(item)
                return True
        return False
    def update_student(self,stu_info):
        for item in self.stu_list:
            if item.id==stu_info.id:
                item.name=stu_info.name
                item.age=stu_info.age
                item.score=stu_info.score
    def output_by_score(self):
        a=self.stu_list[:]
        for r in range(len(a)-1):
            for c in range(r+1,len(a)):
                if a[r].score>a[c].score:
                    a[r],a[c]=a[c],a[r]
        return a


# contriller=StudentMangerController()
# stu01=StudentMode("张无忌",20,100)
# stu02=StudentMode("无忌",10,200)
# stu04=StudentMode("无忌",10,200)
# contriller.add_stu(stu01)
# contriller.add_stu(stu02)
# contriller.add_stu(stu04)
# re=contriller.remove_stu(1)
# stu03=StudentMode("张三",10,200,2)
# stu01=StudentMode("张无忌",20,100)
# contriller.add_stu(stu01)
# contriller.update_student(stu03)
#
#
# for item in contriller.stu_list:
#     print(item.id,item.name,item.age,item.score)
# for item in range(len(contriller.stu_list)):
#     print(item)

class StudentManagerView:
    def __init__(self):
        self.manage=StudentMangerController()
    def __display_menu(self):
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩升序显示")
    def __select_menu_item(self):
        number = input("请输入选项:")
        if number == "1":
            self.__input_student()
        elif number == "2":
            self.__output_student()
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__update_student()
        elif number == "5":
            self.__output_student_by_score()
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_student(self):
        name=input("请输入学生姓名:")
        age=int(input("请输入学生年龄:"))
        score=int(input("请输入学生成绩:"))
        stu=StudentMode(name,age,score)
        self.manage.add_stu(stu)
    def __output_student(self):
        for item in self.manage.stu_list:
            print(item.id,item.name,item.age,item.score)
    def __delete_student(self):
        id=int(input("请输入:"))
        if self.manage.remove_stu(id):
            print("删除成功")
        else:
            print("删除失败")
    def __update_student(self):
        id=int(input("请输入要修改的编号:"))
        name = input("请输入学生姓名:")
        age = int(input("请输入学生年龄:"))
        score = int(input("请输入学生成绩:"))
        stu = StudentMode(name, age, score,id)
        self.manage.update_student(stu)
    def __output_student_by_score(self):
        for item in self.manage.output_by_score():
            print(item.id,item.name,item.age,item.score)
    #     for r in range(len(self.manage.stu_list)-1):
    #         for c in range(r+1,len(self.manage.stu_list)):
    #             if self.manage.stu_list[r].score>self.manage.stu_list[c].score:
    #                 self.manage.stu_list[r],self.manage.stu_list[c]=self.manage.stu_list[c],self.manage.stu_list[r]



view = StudentManagerView()
view.main()

