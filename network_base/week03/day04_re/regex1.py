import re

s="2019年，建国70年"
pattern=r"\d+"

#返回迭代器
it=re.finditer(pattern,s)
for i in it:
    print(i.group())

#完全匹配
m=re.fullmatch(r"\w+","Jame1")
print(m)

#匹配开始位置
m=re.match(r"[A-Z]\w*","Hello,World")
print(m)

#匹配一处
m=re.search(r"[A-Z]\w*","hello Hello,World")
print(m)