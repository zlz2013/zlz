import requests
from lxml import etree
import time,random
from model_tool.useragents import ua_list


class LianjiaSpider():
    def __init__(self):
        self.url='https://sh.lianjia.com/ershoufang/pg{}'
        self.blog=1

    def get_html(self,url):
        headers={'user-agent':random.choice(ua_list)}
        #尝试三次，否则换下一页
        if self.blog<=3:
            try:
                res=requests.get(url=url,headers=headers,timeout=5)
                res.encoding='utf-8'
                html=res.text
                self.parse_page(html)
            except Exception as e:
                print('请求失败')
                self.blog+=1
                self.get_html(url)


    def parse_page(self,html):
        parse_html=etree.HTML(html)
        xpath_1='//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]'
        li_list=parse_html.xpath(xpath_1)
        # print(li_list)
        item={}
        for i in li_list:
            #名称
            print(i)
            name_list=i.xpath(".//a[@data-el='region']/text()")
            print('-'*20)
            print(name_list)
            print('-' * 20)
            # if name_list:
            #     item['name']=name_list[0].strip()
            # else:
            #     item['name']=None

            #使用列表推导式
            print([name_list[0].strip() if name_list else None])
            item['name']=[name_list[0].strip() if name_list else None][0]

            #户型+面积+方位+是否精装
            info_xpath='.//div[@class="houseInfo"]/text()'
            info_list=i.xpath(info_xpath)
            if info_list:
                info_list=info_list[0].strip().split('|')
                if len(info_list)==5:
                    item['model']=info_list[1].strip()
                    item['area']=info_list[2].strip()
                    item['direciton']=info_list[3].strip()
                    item['perfect']=info_list[4].strip()
                else:
                    print(info_list)
                    item['model'] =item['area']=item['direciton']=item['perfect']=None
            else:
                print(info_list)
                item['model'] = item['area'] = item['direciton'] = item['perfect'] = None

            #楼层
            xpath_fool='.//div[@class="positionInfo"]/text()'
            fool_list=i.xpath(xpath_fool)
            item['foor']=[fool_list[0].strip().split()[0] if fool_list else None][0]
            #地区
            xpath_address='.//div[@class="positionInfo"]/a/text()'
            address_list=i.xpath(xpath_address)
            item['address']=[address_list[0].strip() if address_list else None][0]
            # 总价
            total_price_xpath='.//div[@class="totalPrice"]/span/text()'
            total_price_list=i.xpath(total_price_xpath)
            item['total_price'] = [total_price_list[0].strip() if total_price_list else None][0]
            # 单价
            unit_price_xpath='.//div[@class="unitPrice"]/span/text()'
            unit_price_list=i.xpath(unit_price_xpath)
            item['unit_price'] = [unit_price_list[0].strip() if unit_price_list else None][0]
            print(item)
    def main(self):
        for pg in range(1,6):
            url=self.url.format(pg)
            self.get_html(url)
            time.sleep(random.randint(1,3))
            self.blog=1


if __name__=='__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = LianjiaSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end - start))


