# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TencentItem
from urllib import parse
import requests
#导入ｓｃｒａｐｙ_redis中redisspider
#1.
from scrapy_redis.spiders import RedisSpider

#2.继承RedisSpider
class TencentSpider(RedisSpider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    # start_urls = ['http://careers.tencent.com/']
    one_url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url='https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'
    user_input=input('请输入工作类型：')
    user_input = parse.quote(user_input)

    page_one_url=one_url.format(user_input,1)
    #3.去掉start_urls
    # start_urls=[page_one_url]
    #4.设置redis_key
    redis_key = 'tencent:spider'

    #获取总页数
    def get_total(self,user_input):
        url=self.one_url.format(user_input,1)
        html=requests.get(url=url).json()
        total=html['Data']['Count']//10+1
        return total

    #重写start_requests()方法，把一级页面所有地址交给调度器
    def parse(self,response):

        #获取总页数:total
        total=self.get_total(self.user_input)

        for index in range(1,11):
            url=self.one_url.format(self.user_input,index)
            yield scrapy.Request(url=url,callback=self.parse_one_page)


    def parse_one_page(self,response):
        html=response.text
        html=json.loads(html)
        for job in html['Data']['Posts']:
            post_id=job['PostId']
            url=self.two_url.format(post_id)
            yield scrapy.Request(url=url,callback=self.parse_two_page)

    def parse_two_page(self,response):
        item = TencentItem()
        html=json.loads(response.text)
        item['job_name'] = html['Data']['RecruitPostName']
        item['job_type'] = html['Data']['CategoryName']
        item['job_duty'] = html['Data']['Responsibility']
        item['job_require'] = html['Data']['Requirement']
        item['job_address'] = html['Data']['LocationName']
        item['time'] = html['Data']['LastUpdateTime']
        yield item


