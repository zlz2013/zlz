import requests
from lxml import etree


# 程序结构
import time
class RenrenSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.url='http://www.renren.com/971924423/profile'
        self.headers={
            'Cookie':'anonymid=jzc4d44d-q453re; depovince=GW; _r01_=1; JSESSIONID=abcIbjnxwRQ7B9ELxttYw; ick_login=1546bc1c-ce5e-4928-a3cc-e2a4ed276410; t=069c4212ebf45be6a1f404901415302c3; societyguester=069c4212ebf45be6a1f404901415302c3; id=971924423; xnsid=6cb22c4f; jebecookies=0e936e3f-aa3b-41d1-89b4-a03e70eab41a|||||; ver=7.0; loginfrom=null; jebe_key=76ac8b25-e46d-48a3-b1c3-5feb87dd29ba%7C648675a54a44d04fab0ba2a32fdccb2b%7C1565839448058%7C1%7C1565839449131; jebe_key=76ac8b25-e46d-48a3-b1c3-5feb87dd29ba%7C648675a54a44d04fab0ba2a32fdccb2b%7C1565839448058%7C1%7C1565839449133; wp_fold=0',
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
        }

    def get_html(self):
        # 获取响应内容函数,使用随机User-Agent
        html=requests.get(url=self.url,headers=self.headers).text
        self.parse_html(html)

    def parse_html(self,html):
        # 使用正则表达式来解析页面,提取数据
        parse_html=etree.HTML(html)
        r_list=parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li/span[1]/text()')
        print(r_list)

    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    def main(self):
        # 主函数,用来控制整体逻辑
        self.get_html()

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = RenrenSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))