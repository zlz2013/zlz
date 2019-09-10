"""
with    语句示例
"""
#with语句结束，f自动销毁
with open("test") as f:
    data=f.read()
    print(data)