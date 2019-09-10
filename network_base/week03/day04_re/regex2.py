"""
match对象使用示例
"""

import re

pattern=r"(ab)cd(?P<pig>ef)"
regex=re.compile(pattern)
obj=regex.search("abcdefghij")#match对象
print(obj)

#属性变量
print(obj.pos)#目标字符串开头位置
print(obj.endpos)#目标字符串结尾位置
print(obj.re)#正则表达式
print(obj.string)#目标字符串
print(obj.lastgroup)#最后一组的组名
print(obj.lastindex)#最后一组序列号

print(obj.span())#匹配内容的起止位置
print(obj.start())#匹配内容的开始位置
print(obj.end())#匹配内容的结束位置

print(obj.groupdict())#获取捕获组字典，组名为键，内容为名
print(obj.groups())#获取子组对应内容
print(obj.group("pig"))#获取匹配内容