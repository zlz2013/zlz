from selenium import webdriver
# 程序结构
import time
class JdSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        self.url='https://www.jd.com/'
        #设置无界面模式
        self.options=webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.browser=webdriver.Chrome(options=self.options)
        self.n=0

    def get_html(self):
        # 获取响应内容函数,
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        #给商品页面加载时间
        time.sleep(2)

    def parse_html(self):
        # 使用正则表达式来解析页面,提取数据
        #先提取所有商品节点对象列表li列表
        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        item={}
        for li in li_list:
            # print('*'*30)
            # print(li.text)
            # print('*' * 30)
            #find.element:查找单元素
            item['price'] =li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
            item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
            item['commit'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
            item['shopnum'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()
            self.n+=1
            print(item)
        print(self.n)
    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    def main(self):
        # 主函数,用来控制整体逻辑
        self.get_html()
        while True:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            self.parse_html()
            #判断是否为最后一页
            if self.browser.page_source.find('pn-next disable')==-1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(2)
            else:
                break
        print('总共爬取商品数量',self.n)


if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = JdSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))