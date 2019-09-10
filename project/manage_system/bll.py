class StudentMangerController:
  def __init__(self):
    self.stu_list = []

  def stu_list(self):
    return self.stu_list

  def add_stu(self, stu_manege):
    stu_manege.id = self.generate_id()
    self.stu_list.append(stu_manege)

  def generate_id(self):
    return self.stu_list[-1].id + 1 if len(self.stu_list) > 0 else 1

  def remove_stu(self, id):
    for item in self.stu_list:
      if item.id == id:
        self.stu_list.remove(item)
        return True
    return False

  def update_student(self, stu_info):
    for item in self.stu_list:
      if item.id == stu_info.id:
        item.name = stu_info.name
        item.age = stu_info.age
        item.score = stu_info.score

  def output_by_score(self):
    a = self.stu_list[:]
    for r in range(len(a) - 1):
      for c in range(r + 1, len(a)):
        if a[r].score > a[c].score:
          a[r], a[c] = a[c], a[r]
    return a
