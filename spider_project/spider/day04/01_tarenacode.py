import requests
import random,time,os
from lxml import etree
from model_tool.useragents import ua_list


class CodeSpider():
    def __init__(self):
        self.url='http://code.tarena.com.cn/AIDCode/aid1904/15-spider/'
        self.auth=('tarenacode','code_2013')


    def parse_html(self):
        html=requests.get(url=self.url,auth=self.auth,headers={'user-agent':random.choice(ua_list)}).content.decode('utf-8','ignore')
        parse_html=etree.HTML(html)
        r_list=parse_html.xpath('//a/@href')
        for r in r_list:
            if r.endswith('.zip') or r.endswith('.rar'):
                print(r)
                self.save_files(r)

    def save_files(self,r):
        #操作目录，
        dir='/home/tarena/spider/'
        if not os.path.exists(dir):
            os.makedirs(dir)

        #拼接地址，把zip文件保存到制定目录
        url=self.url+r
        filename=dir+r
        html=requests.get(url=url,headers={'user-agent':random.choice(ua_list)},auth=self.auth).content
        with open(filename,'wb') as f:
            f.write(html)
            print("下载成功")


if __name__=="__main__":
    spider=CodeSpider()
    spider.parse_html()
