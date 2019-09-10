"""
flags扩展功能
"""

import re

s="""Hello
上海
"""

#只能匹配ASCII
# regex=re.compile(r"\w+",flags=re.A)
#匹配字母，不区分大小写
# regex=re.compile(r"[A-Z]+",flags=re.I)
#使.可以匹配任意字符
# regex=re.compile(r".+",flags=re.S)
#^$匹配每行开头结尾
# regex=re.compile(r"^\w+\s+\w+$",flags=re.M)
getaren=r"""
        \w+ #匹配
        \s+ #匹配换行
        \w+ #匹配
        """
regex=re.compile(getaren,flags=re.X)


l=regex.findall(s)
print(l)
