#从终端输入一个单词，打印出单词的解释，
# 如果没有该单词，则打印“没有找到该单词”
# find=input("请输入单词:")
# fd=open("dict.txt","r")
# for line in fd:
#     tmp=line.split(" ")[0]
#     if tmp>find:
#         print("没有找到")
#         break
#     elif find==tmp:
#         print(line)
#         break
# else:
#     print("没有找到")

s="a                indef art one"
b=s.split(" ")
c=b[1:]
d=' '.join(c)
e=d.strip()
print(b)
print(c)
print(d)
print(e)
