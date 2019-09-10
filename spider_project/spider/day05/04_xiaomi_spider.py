import requests
from threading import  Thread
from queue import Queue
from fake_useragent import UserAgent
from lxml import etree

# 程序结构
import time
class XiaomiSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.url='http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        #创建队列,存放所有url地址的队列
        self.q=Queue()
        self.n=0
        #存放所有类型ID的空列表
        self.id_list=[]
        self.ua = UserAgent()

    def get_cateid(self):
        url='http://app.mi.com/'
        headers={'user-agent':self.ua.random}
        html=requests.get(url=url,headers=headers).text
        #解析
        parse_html=etree.HTML(html)
        xpath_bds='//ul[@class="category-list"]/li'
        li_list=parse_html.xpath(xpath_bds)

        for li in li_list:
            typ=li.xpath('./a/text()')[0]
            id=li.xpath('./a/@href')[0].split('/')[-1]
            pages=self.get_pages(id)
            self.id_list.append((id,pages))
        self.url_in()

    def get_pages(self,id):
        url=self.url.format(0,id)
        headers = {'user-agent': self.ua.random}
        html=requests.get(url=url,headers=headers).json()
        count=html['count']
        pages=int(count)//30 +1
        return pages

    #url入队列
    def url_in(self):
        for id in self.id_list:
            for page in range(id[1]):
                url=self.url.format(page,id[0])
                #把URL地址入队列
                self.q.put(url)


    #线程事件函数：get() -请求  -解析 -处理数据
    def get_data(self):
        # 获取响应内容函数,使用随机User-Agent
        while True:
            if not self.q.empty():
                url=self.q.get()    #从队列里面获取地址
                headers={'user-agent':self.ua.random}
                html=requests.get(url=url,headers=headers).json()
                self.parse_html(html)
            else:
                break

    def parse_html(self,html):
        # 解析页面,提取数据
        for app in html['data']:
            #获取应用名称
            name=app['displayName']
            link='http://app.mi.com/details?id='+app['packageName']
            print(name,link)
            self.n+=1

    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    def main(self):
        # 主函数,用来控制整体逻辑
        self.get_cateid()
        t_list=[]
        #创建多个线程
        for i in range(8):
            t=Thread(target=self.get_data)
            t_list.append(t)
            t.start()
        #回收线程
        for t in t_list:
            t.join()
        print('数量',self.n)

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))