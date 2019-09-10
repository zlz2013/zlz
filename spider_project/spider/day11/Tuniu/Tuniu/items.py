# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TuniuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 一级页面
    # 标题 + 链接 + 价格 + 满意度 + 出游人数 + 点评人数 + 推荐景点 + 供应商
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    satisfaction = scrapy.Field()
    travelNum = scrapy.Field()
    reviewNum = scrapy.Field()
    recommended = scrapy.Field()
    supplier = scrapy.Field()

    # 二级页面
    # 优惠券 + 产品评论
    coupons = scrapy.Field()
    cp_comments = scrapy.Field()
