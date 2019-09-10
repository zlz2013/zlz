# 程序结构
import time,re,random,csv,pymysql,pymongo
import requests
from lxml import etree

from model_tool.useragents import ua_list


class MaoyanSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.url='https://maoyan.com/board/4?offset={}'
        self.db = pymysql.connect(
            '127.0.0.1','root','123456','maoyandb',charset='utf8'
        )
        self.cursor=self.db.cursor()

        self.page=1

    def get_html(self,url):
        # 获取响应内容函数,使用随机User-Agent
        headers={'user-agent':random.choice(ua_list)}
        # print(headers)
        res=requests.get(url=url,headers=headers)
        res.encoding='utf-8'
        html=res.text
        # print(html)
        self.parse_html(html)

    def parse_html(self,html):
        # 此处用xpath实现，  先基准xpath，在依次遍历
        parse_html0= etree.HTML(html)
        xpath_top100='//div[@class="main"]/dl[@class="board-wrapper"]/dd'
        name_list=parse_html0.xpath(xpath_top100)
        # print(name_list)
        item = {}
        for i in name_list:
            xpath_name='.//p[@class="name"]/a/text()'
            name_maoyan=i.xpath(xpath_name)
            item['name']=[name_maoyan[0].strip() if name_maoyan else None][0]

            xpath_star='.//p[@class="star"]/text()'
            star_maoyan=i.xpath(xpath_star)
            item['star']=[star_maoyan[0].strip() if star_maoyan else None][0]
            xpath_time='.//p[@class="releasetime"]/text()'
            release_time=i.xpath(xpath_time)
            item['time']=[release_time[0].strip() if release_time else None][0]

        #file_list:['电影名'，‘主演’，‘上映时间’]
        print(item)

        #直接调用写入函数
        # self.write_html(film_list)
    def write_html(self,film_list):
        pass
        # 将提取的数据按要求保存,csv、MySQL数据库等
        # film_dict={}
        # for i in film_list:
        #     film_dict['电影名']=i[0].strip()
        #     film_dict['主演']=i[1].strip()[3:]
        #     film_dict['上映时间']=i[2].strip()[5:]
        #     print(film_dict)

        #存csv文件里面
        # list=[]
        # with open('maoyanfilm.csv','a',newline='') as f:
        #     writer=csv.writer(f)
        #     for film in film_list:
        #         one_film=(film[0].strip(),film[1].strip()[3:],film[2].strip()[5:])
        #         list.append(one_film)
        #     writer.writerows(list)

        # 存MySQL数据库里面
        ins='insert into filmtab values(%s,%s,%s)'
        list_maoyan=[]
        for film in film_list:
            l=(
                film[0].strip(),
                film[1].strip()[3:],
                film[2].strip()[5:15]
            )
            list_maoyan.append(l)
        self.cursor.executemany(ins,list_maoyan)
        self.db.commit()


    def main(self):
        # 主函数,用来控制整体逻辑
        for offset in range(0,91,10):
            url=self.url.format(offset)
            self.get_html(url)
            time.sleep(random.randint(1,2))

        #断开数据库连接
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))