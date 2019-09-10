# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class DaomuPipeline(object):
    def process_item(self, item, spider):
        print(item['name'],item['content'])


        filename='/home/tarena/novel/'+item['name'].strip().replace(' ','-')+'.txt'
        with open(filename,'w')as f:
            f.write(item['content'])
        return item
