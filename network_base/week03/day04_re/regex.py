import re

s="校长:1993,小李:1994"
pattern=r"(\w+):(\d+)"

#re模块调用findall
l=re.findall(pattern,s)
print(l)

#使用compile对象调用
regex=re.compile(pattern)
l=regex.findall(s,0,6)
print(l)

#按照匹配到的内容切割字符串
l=re.split(r"[:,]",s)
print(l)

#替换匹配到的内容
s=re.sub(r"\s+","#","this is a test",1)
print(s)

#替换匹配到的内容
s=re.subn(r"\s+","#","this is a test",1)
print(s)

str="fnids afd sa 2019-05-23,2019-06-13,-0.2,2019-06-"
pattern=r"\d{4}-\d{2}-\d{2}"
l=re.findall(pattern,str)
for i in l:
    s=re.sub(r"-","/",i)
    print(s)