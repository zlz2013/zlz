# 程序结构
import time
import requests
from fake_useragent import UserAgent




class DoubanSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.base_url='https://movie.douban.com/j/chart/top_list?'
        self.i=0

    def get_html(self,params):
        # 获取响应内容函数,使用随机User-Agent
        ua=UserAgent()
        headers={'user-agent':ua.random}
        res=requests.get(url=self.base_url,params=params,headers=headers)
        res.encoding='utf-8'
        html=res.json()
        self.parse_html(html)


    def parse_html(self,html):
        # 使用正则表达式来解析页面,提取数据
        item={}
        for one in html:
            item['name']=one['title']
            item['score']=one['score']
            item['time']=one['release_date']
            print(item)
            self.i+=1

    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    #获取电影总数
    def get_total(self,typp):
        url='https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(typp)
        ua=UserAgent()
        html=requests.get(url=url,headers={'user-agent':ua.random}).json()
        total=html['total']
        print(total)
        return total

    def main(self):
        # 主函数,用来控制整体逻辑
        typ=input('请输入电影类型（剧情|喜剧|动作）')
        typ_dict={'剧情':'11','喜剧':'24','动作':'5'}
        typp=typ_dict[typ]
        total=self.get_total(typp)
        for page in range(0,int(total),20):
            params={
                'type': typp,
                'interval_id': '100:90',
                'action':'',
                'start':str(page),
                'limit': '20'
            }
            self.get_html(params)
            time.sleep(1)
        print('数量',self.i)
if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = DoubanSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))