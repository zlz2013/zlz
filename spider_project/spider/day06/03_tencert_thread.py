import requests
import json
import time
import random
from model_tool.useragents import ua_list
from threading import Thread
from queue import Queue


class TencentSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.one_url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1565833768838&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url='https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1565835413447&postId={}&language=zh-cn'
        self.headers={'user-agent':random.choice(ua_list)}
        self.q=Queue()

    def get_page(self,url):
        # 获取响应内容函数,使用随机User-Agent
        html=requests.get(url=url,headers=self.headers).text
        #json格式字符串转为Python数据类型
        html=json.loads(html)
        return html

    #主线函数:获取所有数据
    def parse_page(self):
        # 使用正则表达式来解析页面,提取数据
        while True:
            if not self.q.empty():
                one_url=self.q.get()

                html=self.get_page(one_url)
                item={}
                for job in html['Data']['Posts']:
                    #名称
                    item['name']=job['RecruitPostName']
                    #postid
                    post_id=job['PostId']
                    #拼接二级地址，获取职责和要求
                    two_url=self.two_url.format(post_id)
                    item['duty'],item['require']=self.parse_twopage(two_url)
                    print(item)
            else:
                break


    def parse_twopage(self,two_url):
        html=self.get_page(two_url)
        duty=html['Data']['Responsibility']
        duty=duty.replace('\r\n','').replace('\n','')
        require=html['Data']['Requirement']
        require=require.replace('\r\n','').replace('\n','')
        return duty,require


    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    def get_number(self):
        url=self.one_url.format(1)
        html = self.get_page(url)
        count = int(html['Data']['Count'])//10 +1
        return count
    def main(self):
        #url入队列
        pages=self.get_number()
        # 主函数,用来控制整体逻辑
        for page in range(1,pages+1):
            one_url=self.one_url.format(page)

            self.q.put(one_url)

        t_list=[]
        for i in range(5):
            t=Thread(target=self.parse_page)
            t_list.append(t)
            t.start()
        for t in t_list:
            t.join()


if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = TencentSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))