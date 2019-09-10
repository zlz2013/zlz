
def dict(find):
    fd=open("dict.txt","r")
    for line in fd:
        tmp=line.split(" ")[0]
        if tmp>find:
            return "没有找到"
        elif find==tmp:
            return line
    else:
        return "没有找到"

find=input("请输入单词:")
dict(find)