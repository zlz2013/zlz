import urllib.request

url1='http://httpbin.org/get'

response=urllib.request.urlopen(url1)
print(response)

#获取响应对象内容
html=response.read().decode('utf-8')
print(html)

#获取http响应码
code=response.getcode()
print(code)

#获取返回实际数据的URL地址
url=response.geturl()
print(url)