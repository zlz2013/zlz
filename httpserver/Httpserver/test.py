"""
用于httpserver的检测
"""

from socket import *
import json

s=socket()
s.bind(('0.0.0.0',8080))
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.listen(3)
c,addr=s.accept()
data=c.recv(1024).decode()
print(data)
d={'status': '200', 'data': 'from test'}
data=json.dumps(d)
c.send(data.encode())

c.close()
s.close()