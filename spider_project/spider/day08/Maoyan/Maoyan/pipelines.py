# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from .settings import *
class MaoyanPipeline(object):
    #item：从爬虫文件maoyan.py中yield的item数据
    def process_item(self, item, spider):
        print(item['name'],item['time'],item['star'])
        return item

#自定义管道-将数据存入数据库
class MaoyanMysqlpipeline(object):

    #爬虫项目开始运行时，执行此函数
    def open_spider(self,spider):
        print('我是open_spider函数的输出')
        #一般用于建立数据库链接
        self.db=pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQL_CHAR,
        )
        self.cursor=self.db.cursor()
    def process_item(self,item,spider):
        print('我是process_item函数的输出')
        ins='insert into filmtab values(%s,%s,%s)'
        L=[item['name'],item['star'],item['time']]
        self.cursor.execute(ins,L)
        self.db.commit()
        return item
    #爬虫项目结束时，执行此函数
    def close_spider(self,spider):
        print('我是close_spider函数的输出')
        #一般用于断开数据库链接
        self.cursor.close()
        self.db.close()