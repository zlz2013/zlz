from selenium import webdriver
import time

class JdSpider():
    def __init__(self):
        self.browser=webdriver.Chrome()
        self.url='https://www.jd.com/'
        self.i=0

    def get_page(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书籍')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    def parse_page(self):
        #解析页面
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)

        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            li_info=li.text.split('\n')
            if li_info[0][0:2]=='每满':
                price=li_info[1]
                name=li_info[2]
                commit=li_info[3]
                market=li_info[4]
            else:
                price = li_info[0]
                name = li_info[1]
                commit = li_info[2]
                market = li_info[3]

        print('\033[31m*********************\033[0m')
        print(price)
        print(name)
        print(commit)
        print(market)
        self.i+=1
    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            if self.browser.page_source.find('pn-next disabled')==-1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(2)
            else:
                break
        print(self.i)

if __name__=="__main__":
    start = time.time()
    spider = JdSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end - start))