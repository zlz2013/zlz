"""
2048游戏核心算法
"""
# 1.定义函数，将列表中0元素移至末尾
# 【2,0,2,0】-->[2,2,0,0]
# 【2,0,0,2】-->[2,2,0,0]
# 【2,4,0,2】-->[2,2,0,0]




# def zero_remove_end():
#     for i in range(len(list01) - 1, -1, -1):
#         if list01[i] == 0:
#             del list01[i]
#             list01.append(0)
#
# list01=[2,4,0,2]
# zero_remove_end()
# print(list01)



# def zero_remove_end(list01):
#     for i in range(len(list01) - 1, -1, -1):
#         if list01[i] == 0:
#             del list01[i]
#             list01.append(0)
#     return list01
# def two_add(list01):
#     list02=zero_remove_end(list01)
#     for i in range(len(list02)-1):
#         if list02[i]==list02[i+1]:
#             list02[i]+=list02[i+1]
#             del list02[i+1]
#             list02.append(0)
#
# list01=[2,2,2,2]
# zero_remove_end(list01)
# two_add(list01)
# print(list01)



# def zero_remove_end(list01):
#     for l in range(len(list01)):
#         for i in range(len(list01[l]) - 1, -1, -1):
#             if list01[l][i] == 0:
#                 del list01[l][i]
#                 list01[l].append(0)
#     return list01
# # def two_add(list01):
# #     list02=zero_remove_end(list01)
# #     for i in range(len(list02)-1):
# #         if list02[i]==list02[i+1]:
# #             list02[i]+=list02[i+1]
# #             del list02[i+1]
# #             list02.append(0)

def zero_remove_end(list01):
    for i in range(len(list01) - 1, -1, -1):
        if list01[i] == 0:
            del list01[i]
            list01.append(0)
    return list01
def two_add(list01):
    zero_remove_end(list01)
    for i in range(len(list01)-1):
        if list01[i]==list01[i+1]:
            list01[i]+=list01[i+1]
            del list01[i+1]
            list01.append(0)

def move_left(map):
    for row in map:
        two_add(row)
def move_right(map):
    for i in range(len(map)):
        list02=map[i][::-1]
        two_add(list02)
        map[i][::-1]=list02

        print(list02)
def move_down(map):
    #30 20 10 00
    for r in range(4):
        new_list=[]
        for c in range(3,-1,-1):
            new_list.append(map[c][r])
        two_add(new_list)
        for c in range(3,-1,-1):
            map[c][r]=new_list[3-c]
def move_up(map):
    #00 10 20 30
    for r in range(4):
        new_list=[]
        for c in range(4):
            new_list.append(map[c][r])
        two_add(new_list)
        for c in range(4):
            map[c][r]=new_list[c]
list01=[
    [0,2,2,2],
    [0,2,0,4],
    [2,0,4,2],
    [0,4,2,2]
]
# move_left(list01)
# move_right(list01)
# two_add(list01)
move_down(list01)
# move_up(list01)

print(list01)