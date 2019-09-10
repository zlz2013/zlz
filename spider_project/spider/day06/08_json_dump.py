import json
#示例1
# item={'name':'金毛狮王','card':'屠龙刀'}
# with open('yt.json','a')as f:
#     json.dump(item,f,ensure_ascii=False)


#json.load()把文件中JSON串读取出来并转为Python数据类型
with open('yt.json','r')as f :
    res=json.load(f)

print(res)
print(type(res))



#示例2
item_list=[
    {'name':'金毛狮王','card':'屠龙刀'},
    {'name':'紫衫龙王','card':'倚天剑'},
]

with open('yt.json','w')as f:
    json.dump(item_list,f,ensure_ascii=False)


