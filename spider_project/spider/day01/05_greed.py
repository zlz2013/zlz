import re

html='''
<div><p>九霄龙吟惊天变</p></div>
<div><p>风云际会潜水游</p></div>
'''

#贪婪匹配
pattern=re.compile('<div><p>(.*)</p></div>',re.S)
r_list=pattern.findall(html)
print(r_list)

#非贪婪匹配
pattern=re.compile('<div><p>(.*?)</p></div>',re.S)
r_list=pattern.findall(html)
print(r_list)


s = 'A B C D E F'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))