from selenium import webdriver

import pymysql

# 程序结构
import time
class GovSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.browser=webdriver.Chrome()
        self.one_url='http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.db = pymysql.connect('127.0.0.1', 'root', '123456', 'govdb', charset='utf8')
        self.cursor = self.db.cursor()

        self.province_list=[]
        self.city_list=[]
        self.county_list=[]

    def get_incr_url(self):
        # 获取响应内容函数
        self.browser.get(self.one_url)
        #提取最新链接，判断是否需要增量爬
        td=self.browser.find_element_by_xpath('//td[@class="arlisttd"]/a[contains(@title,"代码")]')
        #提取链接和数据库中做比对，来确定是否需要增量抓取
        #get_attribute:会自动不全提取的连接
        two_url=td.get_attribute('href')
        print(two_url)
        sel='select url from version where url=%s'
        res =self.cursor.execute(sel,[two_url])
        # self.cursor.fetchall()
        #res:为返回的受影响的条数
        print(res)
        if res:
            print('已是最新，无需爬取')
        else:
            td.click()
            #切换句柄
            all_handlers=self.browser.window_handles
            self.browser.switch_to.window(all_handlers[1])
            self.get_data()
            #把URL地址存入到version表中
            delete='delete from version'
            ins='insert into version values(%s)'
            self.cursor.execute(delete)
            self.cursor.execute(ins,[two_url])
            self.db.commit()


    def get_data(self):
        #
        tr_list=self.browser.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            code=tr.find_element_by_xpath('./td[2]').text
            name=tr.find_element_by_xpath('./td[3]').text
            print(code,name)
            if code[-4:]=='0000':
                self.province_list.append([name,code])
                if name in ['北京市','天津市','重庆市','上海市']:
                    self.city_list.append([name,code,code])

            elif code[-2:]=='00':
                self.city_list.append([name,code,(code[:2]+'0000')])
            else:
                if code[:2] in ['11','12','31','50']:
                    self.county_list.append([name,code,(code[:2]+'0000')])
                else:
                    self.county_list.append([name,code,(code[:4]+'00')])

        #执行数据库插入语句
        self.insert_mysql()

    def insert_mysql(self):
        del_province='delete from province'
        del_city='delete from city'
        del_county='delete from county'
        self.cursor.execute(del_province)
        self.cursor.execute(del_city)
        self.cursor.execute(del_county)
        #插入新数据
        ins_province='insert into province values(%s,%s)'
        ins_city='insert into city values(%s,%s,%s)'
        ins_county='insert into county values(%s,%s,%s)'
        self.cursor.execute(ins_province,self.province_list)
        self.cursor.execute(ins_city,self.city_list)
        self.cursor.execute(ins_county,self.county_list)
        #提交到数据库执行
        self.db.commit()

    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    def main(self):
        # 主函数,用来控制整体逻辑
        self.get_incr_url()
        self.get_data()

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = GovSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))