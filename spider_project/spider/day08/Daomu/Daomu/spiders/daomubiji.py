# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem
import os
class DaomubijiSpider(scrapy.Spider):
    name = 'daomubiji'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    #判断路径是否存在
    directory = '/home/tarena/novel/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    def parse(self, response):
        #解析一级页面，提取11个链接，交给调度器入队列

        one_link=response.xpath('//li[contains(@class,"menu-item-20")]/a/@href').extract()
        print('*'*20)
        print(one_link)
        print('*' * 20)
        for one in one_link:
            print(one)
            yield scrapy.Request(url=one,callback=self.parse_two_page)

    #最终目标:名字+链接
    def parse_two_page(self,response):
        #基准xpath
        article_list=response.xpath('//article')
        for article in article_list:
            print(article)
            item=DaomuItem()
            item['name']=article.xpath('./a/text()').get()
            two_link=article.xpath('./a/@href').get()
            print(item['name'])
            #把链接在发给调度器
            yield scrapy.Request(url=two_link,
                                 callback=self.parse_three_page,
                                 #在不同解析函数之间传递item对象
                                 meta={'item':item},
                                 )

    def parse_three_page(self,response):
        #取出item对象
        item=response.meta['item']
        p_list=response.xpath('//article[@class="article-content"]/p/text()').extract()
        item['content']=''.join(p_list)
        print(item['content'])
        yield item