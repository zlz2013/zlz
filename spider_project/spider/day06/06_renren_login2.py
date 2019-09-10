import time

import requests
from lxml import etree


class RenrenSpider():
    def __init__(self):
        self.url='http://www.renren.com/PLogin.do'
        self.get_url='http://www.renren.com/971924423/profile'
        #实例化session对象
        self.session=requests.session()

    def get_html(self):
        #email和password中
        form_data={
            'email':'229165631@qqcom',
            'password':''
        }
        #先session.post()
        self.session.post(url=self.url,data=form_data)
        #再session.get()
        html=self.session.get(url=self.get_url).text
        self.parse_html(html)

    def parse_html(self, html):
        # 使用正则表达式来解析页面,提取数据
        print(html)
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li/span[1]/text()')
        print(r_list)

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
    print('执行时间:%.2f' % (end - start))