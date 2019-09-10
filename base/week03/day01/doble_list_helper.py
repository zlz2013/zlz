"""
4.(扩展)
    定义函数,获取二维列表,某个位置元素的某个方向,的指定个数的所有元素.
    例如:获取下列二维列表,21位置元素,向右,3
     结果: 22   23  24

      00   01   02   03  04
      10   11   12   13  14
      20   21   22   23  24
"""


class Vector2:
  """
    向量
  """

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @staticmethod
  def get_right():
    return Vector2(0, 1)

  @staticmethod
  def get_up():
    return Vector2(-1, 0)

  @staticmethod
  def get_left():
    return Vector2(0, -1)

  @staticmethod
  def get_down():
    return Vector2(1, 0)

#10:55 上课
def get_elements(target, vect_pos, vect_dir, count):
  """
  获取二维列表中，某个位置，某个方向，指定数量的向量
  :param target:
  :param vect_pos:
  :param vect_dir:
  :param count:
  :return:
  """
  result = []
  for i in range(count):
    # 改变位置:原位置 + 方向
    vect_pos.x += vect_dir.x
    vect_pos.y += vect_dir.y
    result.append(target[vect_pos.x][vect_pos.y])
  return result


