"""
select 示例
"""

from select import select
from socket import *

s=socket()
s.bind(("0.0.0.0",8888))
s.listen(3)

print("监控IO")
rs,ws,xs=select([s],[],[],3)
print("rslist:",rs)
print("wslist:",ws)
print("xslist:",xs)
