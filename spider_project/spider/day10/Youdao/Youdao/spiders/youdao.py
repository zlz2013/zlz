# -*- coding: utf-8 -*-
import random
import time
from hashlib import md5

import json
import scrapy
from ..items import YoudaoItem


class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    start_urls = ['http://fanyi.youdao.com/']

    word = input('请输入要翻译的单词:')
    def get_salt_sign_ts(self,word):
        #ts
        ts=str(int(time.time()*1000))
        #salt
        salt = ts + str(random.randint(0, 9))
        #sign
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        return salt, sign, ts

    def start_requests(self):
        post_url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        salt, sign, ts = self.get_salt_sign_ts(self.word)
        formdata={
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': 'cf156b581152bd0b259b90070b1120e6',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        # cookies=self.get_cookies()
        yield scrapy.FormRequest(url=post_url,
                                 formdata=formdata,
                                 callback=self.parse
                                 # cookies=cookies
                                 )

    def get_cookies(self):
        string="OUTFOX_SEARCH_USER_ID=719627021@10.169.0.83; JSESSIONID=aaakMEEqIJOxOazJkikYw; OUTFOX_SEARCH_USER_ID_NCOO=1747473194.4334164; ___rl__test__cookies=1565685533880"
        cookies={}
        for s in string.split('; '):
            cookies[s.split('=')[0]]=s.split('=')[1]

        return cookies



    def parse(self, response):
        item = YoudaoItem()
        html = json.loads(response.text)
        item['result'] = html['translateResult'][0][0]['tgt']
        yield item
