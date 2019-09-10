import requests

url='http://www.baidu.com/'

headers={
    'user-agent':'mozilla/5.0'
}

res=requests.get(url=url,headers=headers)
#显示编码
res.encoding='utf-8'    #设置编码
print(res.encoding)

# print(res.text)   #获取文本内容 -string
# print(res.headers)    #获取请求头
# print(res.content)    #获取文本内容 -byte
print(res.status_code)
print(res.url)
