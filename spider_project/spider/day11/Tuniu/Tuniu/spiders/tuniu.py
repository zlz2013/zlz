# -*- coding: utf-8 -*-
import scrapy
from ..config import *
from ..items import TuniuItem
import json

class TuniuSpider(scrapy.Spider):
    name = 'tuniu'
    allowed_domains = ['tuniu.com']
    # start_urls = ['http://tuniu.com/']

    def start_requests(self):
        s_city = input('出发城市:')
        d_city = input('相关目的地:')
        start_time = input('出发时间(20190828):')
        end_time = input('结束时间(例如20190830):')
        s_city = src_citys[s_city]
        d_city = dst_citys[d_city]
        url = 'http://s.tuniu.com/search_complex/whole-sh-0-%E7%83%AD%E9%97%A8/list-a{}_{}-{}-{}'.format(start_time,end_time,s_city, d_city)
        print(url)
        yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # 提取所有景点的li节点信息列表
        items = response.xpath('//ul[@class="thebox clearfix"]/li')
        for item in items:
            # 此处是否应该在for循环内创建?
            tuniuItem = TuniuItem()
            # 景点标题 + 链接 + 价格
            tuniuItem['title'] = item.xpath('.//span[@class="main-tit"]/@name').get()
            tuniuItem['link'] = 'http:' + item.xpath('./div/a/@href').get()
            tuniuItem['price'] =int(item.xpath('.//div[@class="tnPrice"]/em/text()').get())
            # 判断是否为新产品
            isnews = item.xpath('.//div[@class="new-pro"]').extract()

            if not len(isnews):
                # 满意度 + 出游人数 + 点评人数
                tuniuItem['satisfaction'] = item.xpath('.//div[@class="comment-satNum"]//i/text()').get()
                tuniuItem['travelNum'] = item.xpath('.//p[@class="person-num"]/i/text()').get()
                tuniuItem['reviewNum'] = item.xpath('.//p[@class="person-comment"]/i/text()').get()
            else:
                tuniuItem['satisfaction'] = '新产品'
                tuniuItem['travelNum'] = '新产品'
                tuniuItem['reviewNum'] = '新产品'

            # 包含景点+供应商
            tuniuItem['recommended'] = item.xpath('.//span[@class="overview-scenery"]/text()').extract()
            tuniuItem['supplier'] = item.xpath('.//span[@class="brand"]/span/text()').extract()

            yield scrapy.Request(tuniuItem['link'], callback=self.item_info, meta={'item': tuniuItem})

        # 解析二级页面
    def item_info(self, response):
        tuniuItem = response.meta['item']
        # 优惠信息
        coupons = ','.join(response.xpath('//div[@class="detail-favor-coupon-desc"]/@title').extract())
        tuniuItem['coupons'] = coupons

        # 想办法获取评论的地址
        # 产品点评 + 酒店点评 + 景点点评
        productId = response.url.split('/')[-1]
        print(response.url)
        # 产品点评
        cpdp_url = 'http://www.tuniu.com/papi/tour/comment/product?productId={}'.format(productId)

        yield scrapy.Request(cpdp_url, callback=self.cpdp_func, meta={'item': tuniuItem})

        # 解析产品点评

    def cpdp_func(self, response):
        tuniuItem = response.meta['item']

        html = json.loads(response.text)
        comment = {}
        for s in html['data']['list']:
            comment[s['realName']] = s['content']

        tuniuItem['cp_comments'] = comment

        yield tuniuItem