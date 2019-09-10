# 程序结构
import time,re,random,csv,pymysql,pymongo
from urllib import request

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
        print(headers)
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')
        self.parse_html(html)

    def parse_html(self,html):
        # 使用正则表达式来解析页面,提取数据
        re_bds=r'<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern=re.compile(re_bds,re.S)
        #file_list:['电影名'，‘主演’，‘上映时间’]
        film_list=pattern.findall(html)
        print(film_list)
        #直接调用写入函数
        self.write_html(film_list)
    def write_html(self,film_list):
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