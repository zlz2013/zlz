from bll import *
from model import *
class StudentManagerView:
  def __init__(self):
    self.manage = StudentMangerController()

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
    name = input("请输入学生姓名:")
    # age = int(input("请输入学生年龄:"))
    age=self.__input_number("请输入学生年龄:")
    # score = int(input("请输入学生成绩:"))
    score=self.__input_number("请输入学生成绩:")
    stu = StudentMode(name, age, score)
    self.manage.add_stu(stu)

  def __output_student(self):
    for item in self.manage.stu_list:
      print(item.id, item.name, item.age, item.score)

  def __delete_student(self):
    id = int(input("请输入:"))
    if self.manage.remove_stu(id):
      print("删除成功")
    else:
      print("删除失败")

  def __update_student(self):
    id = int(input("请输入要修改的编号:"))
    name = input("请输入学生姓名:")
    # age = int(input("请输入学生年龄:"))
    age=self.__input_number("请输入学生年龄:")
    score = int(input("请输入学生成绩:"))
    stu = StudentMode(name, age, score, id)
    self.manage.update_student(stu)

  def __output_student_by_score(self):
    for item in self.manage.output_by_score():
      print(item.id, item.name, item.age, item.score)
  def __input_number(self,str_number):
    while True:
      try:
        number = int(input(str_number))
        return number
      except:
        print("输入有误,请重新输入！")



