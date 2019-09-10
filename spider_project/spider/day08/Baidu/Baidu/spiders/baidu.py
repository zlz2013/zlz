# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    #爬虫名：scrapy crawl 爬虫名
    name = 'baidu'
    #允许爬取的域名
    allowed_domains = ['www.baidu.com']
    #第一个要爬取的URL地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        #response为百度的响应对象，从响应对象中提取想要的数据
        xpath_bds='/html/head/title/text()'
        #extract():【‘百度一下，你就知道’】
        #extract_first():'百度一下，你就知道'
        # r_list=response.xpath(xpath_bds).extract_first()
        #1.6版本后可使用get():'百度一下，你就知道'
        r_list=response.xpath(xpath_bds).get()
        print('*'*30)
        print(r_list)
        print('*' * 30)
