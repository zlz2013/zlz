import random
from model import Location
class GameCoreController:
    def __init__(self):
        self.map=[
            [0,0,0,0],
            [0]*4,
            [0]*4,
            [0]*4,
        ]
        #定义空列表用于存储去0以及合并
        self.list_marge=[]
        #定义空列表用于存储空位置
        self.list_empty_location=[]
        #地图是否发生变化
        self.map_is_change=False
    def generate_new_number(self):
        #随机生成新数字
        self.get_empty_location()
        if len(self.list_empty_location)==0:
            return
        loc=random.choice(self.list_empty_location)
        self.map[loc.r_index][loc.c_index]=4 if random.randint(1,10)==1 else 2
        self.list_empty_location.remove(loc)
    def get_empty_location(self):
        self.list_empty_location.clear()
        for r in range(4):
            for c in range(4):
                if self.map[r][c]==0:
                    loc=Location(r,c)
                    self.list_empty_location.append(loc)



def print_map(map):
    print("----------------")
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c], end=" ")
        print()
a=GameCoreController()
print_map(a.map)
a.generate_new_number()
a.generate_new_number()
print_map(a.map)

