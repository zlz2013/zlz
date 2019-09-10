# -*- coding: utf-8 -*-
import scrapy


class TextSpider(scrapy.Spider):
    name = 'text'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print('我是ｐａｒｓｅ函数的输出')
