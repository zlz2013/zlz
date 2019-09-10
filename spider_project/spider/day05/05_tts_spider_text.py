import requests
from lxml import etree

# 程序结构
import time
class ttsSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.url = 'http://www.tmooc.cn/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        }
        self.data={
            'loginName': '229165631@qq.com',
            'password': '25f9e794323b453885f5181f1b624d0b',
            'imgCode':'',
            'accountType': '1'
        }
        self.auth=('229165631@qq.com','123456789')

    def get_html(self):
        # 获取响应内容函数,使用随机User-Agent
        res = requests.get(url=self.url, auth=self.auth, headers=self.headers)
        res.encoding='utf-8'
        html = res.text
        print(html)

    def parse_html(self):
        # 使用正则表达式来解析页面,提取数据
        pass

    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    def main(self):
        # 主函数,用来控制整体逻辑
        self.get_html()

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider =ttsSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))