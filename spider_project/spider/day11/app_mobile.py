import requests
from lxml import etree

post_url='http://m.youdao.com/translate'

word=input('请输入要翻译的单词：')
post_data={
    'inputtext': word,
    'type': 'AUTO',
}

html=requests.post(url=post_url,data=post_data).text
parse_html=etree.HTML(html)
res=parse_html.xpath('//*[@id="translateResult"]/li/text()')[0]
print(res)