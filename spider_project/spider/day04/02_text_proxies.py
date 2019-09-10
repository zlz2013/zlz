#使用代理IP访问测试网站，查看结果
import requests


url='http://httpbin.org/get'
proxies={
    'http':'http://211.159.171.58:80',
    'https':'https://60.13.42.22:9999'
}

#发请求，获取响应内容，查看origin IP
html=requests.get(url=url,proxies=proxies,timeout=8).text
print(html)