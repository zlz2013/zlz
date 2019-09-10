import requests
from lxml import etree
import time,random
from fake_useragent import UserAgent

class GetProxyIP():
    def __init__(self):
        self.url='https://www.xicidaili.com/nn/{}'
        self.proxies={
            'http':'http://{}:{}',
            'https':'https://{}:{}'
        }
    #
    def get_random_ua(self):
        ua=UserAgent()
        useragent=ua.random
        return useragent

    #获取可用代理IP文件
    def get_ip_file(self,url):
        headers={'user-agent':self.get_random_ua()}
        html=requests.get(url=url,headers=headers).text
        parse_html=etree.HTML(html)
        tr_list=parse_html.xpath('//tr')
        for tr in tr_list[1:]:
            ip=tr.xpath('./td[2]/text()')[0]
            port=tr.xpath('./td[3]/text()')[0]

            self.text_ip(ip,port)

    def text_ip(self,ip,port):
        #res.status_code==200
        proxies={
            'http':'http://{}:{}'.format(ip,port),
            'https':'https://{}:{}'.format(ip,port)
        }
        test_url='http://www.baidu.com'
        res=requests.get(url=test_url,proxies=proxies,timeout=8)

        try:
            if res.status_code=='200':
                print(ip,port,'success')
                with open('proxies.txt','a') as f:
                    f.write(ip+':'+port+'\n')
            else:
                print(ip,port,'feiled')
        except Exception as e:
            print(ip,port,'feiled')



    def main(self):
        for i in range(1,100):
            url=self.url,format(i )
            self.get_ip_file(url)
            time.sleep(random.randint(5,10))


if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = GetProxyIP()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))