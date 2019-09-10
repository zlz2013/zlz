import time,re
import requests
from lxml import etree
import pymysql

class GovementSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.url='http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers={'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
        self.db=pymysql.connect('127.0.0.1','root','123456','govdb',charset='utf8')
        self.cursor=self.db.cursor()

    #获取假连接
    def get_false_link(self):
        html=requests.get(url=self.url,headers=self.headers).text
        #解析
        parse_html=etree.HTML(html)
        a_list=parse_html.xpath('//a[@class="artitlelist"]')
        for a in a_list:
            #title = a.xpath('./@title') 与下一行代码等同
            #get()方法：获取某个属性的值
            title=a.get('title')
            if title.endswith('代码'):
                false_link='http://www.mca.gov.cn'+a.get('href')
                break

        self.incr_spider(false_link)

    def incr_spider(self, false_link):
        sel = 'select url from version where url=%s'
        self.cursor.execute(sel,false_link)
        # fetchall:((http://xxx.html))
        result = self.cursor.fetchall()
        if not result:  # 代表数据库version表中没有数据
            self.get_true_link(false_link)

            #可选操作：数据库version表中只保留最新1条数据
            delete='delete from version'
            self.cursor.execute(delete)

            # 把爬取后的连接插入到数据库中
            ins = 'insert into version values(%s)'
            self.cursor.execute(ins, [false_link])
            self.db.commit()
        # 获取真连接存数据库之前判断
        # 在数据表中有没有

        # 把连接存入数据库中一份
        else:
            print('数据已是最新，无需爬取')

    # 获取真连接
    def get_true_link(self,false_link):
        #先获取假链接的响应，然后根据响应获取真连接
        html=requests.get(url=false_link,headers=self.headers).text
        # print(html)
        # with open('false_link.html','w') as f:
        #     f.write(html)

        #利用正则提取真实连接
        re_bds=r'window.location.href="(.*?)"'
        pattern=re.compile(re_bds,re.S)
        true_link=pattern.findall(html)[0]
        print(true_link)
        self.save_data(true_link)



    #数据提取
    def save_data(self,true_link):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        html=requests.get(url=true_link,headers=self.headers).text

        #增量爬去数据

        #用xpath提取数据
        parse_html=etree.HTML(html)
        t_list=parse_html.xpath('//tr[@height="19"]')
        for tr in t_list:
            code=tr.xpath('./td[2]/text()')[0].strip()
            city=tr.xpath('./td[3]/text()')[0].strip()
            print(code,city)


    def main(self):
        # 主函数,用来控制整体逻辑
        self.get_false_link()

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = GovementSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))