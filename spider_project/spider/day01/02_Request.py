from urllib import request

url='http://httpbin.org/get'
headers={'user-agent':'111'}

#创建请求对象,包装，并没有真正发送请求
req=request.Request(url,headers=headers)
#获取响应对象
res=request.urlopen(req)
#获取响应内容
html=res.read().decode('utf-8')
print(html)

url1='https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87'