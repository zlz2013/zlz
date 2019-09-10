import requests
from lxml import etree
import time,random
from model_tool.useragents import ua_list

class BijiSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.url='http://code.tarena.com.cn/AIDCode/aid1904/15-spider/'
        self.auth=('tarenacode','code_2013')

    def get_html(self):
        # 获取响应内容函数,使用随机User-Agent
        headers={'user-agent':random.choice(ua_list)}
        html=requests.get(url=self.url,headers=headers,auth=self.auth).text
        return html

    def parse_html(self):
        # 使用正则表达式来解析页面,提取数据
        html=self.get_html()
        xpath_dbs='//a/@href'
        parse_html=etree.HTML(html)
        r_list=parse_html.xpath(xpath_dbs)
        print(r_list)
        for i in r_list:
            if i.endswith('.zip') or i.endswith('.rar'):
                file_url=self.url+i
                self.write_html(file_url,i)



    def write_html(self,file_url,i):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        headers = {'user-agent': random.choice(ua_list)}
        html_content=requests.get(url=file_url,headers=headers,auth=self.auth).content

        with open('./biji/'+i,'wb') as f:
            f.write(html_content)
            print('下载成功')
    def main(self):
        # 主函数,用来控制整体逻辑
        self.parse_html()

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = BijiSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))