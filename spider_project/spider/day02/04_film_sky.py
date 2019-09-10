from urllib import request
import re,time,random
from model_tool.useragents import ua_list

class FilmSkySpider():
    def __init__(self):
        self.url='https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'


    #获取响应内容函数
    def get_html(self,url):
        headers={'user-agent':random.choice(ua_list)}
        req=request.Request(url=url,headers=headers)
        res=request.urlopen(req)
        html=res.read().decode('gb2312','ignore')

        return html

    #正则解析的功能函数
    def re_func(self,re_bds,html):
        pattern=re.compile(re_bds,re.S)
        r_list=pattern.findall(html)

        return r_list


    #获取数据函数--html是一级页面响应内容
    def parse_page(self,html):
        #想办法获取到电影名称和下载连接
        re_bds=r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">(.*?)</a>.*?</table>'
        #one_page_list=['html地址','电影名']
        one_page_list=self.re_func(re_bds,html)
        item={}
        for film in one_page_list:
            item['电影名']=film[1].strip()
            # '电影名下载链接'
            link='https://www.dytt8.net'+film[0].strip()
            item['下载链接']=self.parse_two_page(link)

            # uniform:浮点数，爬取一个电影信息后sleep
            time.sleep(random.uniform(1, 3))
            print(item)

    #解析二级页面数据
    def parse_two_page(self,link):
        html=self.get_html(link)
        re_bds=r'<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
        # two_page_list=['下载连接']
        two_page_list=self.re_func(re_bds,html)
        download=two_page_list[0].strip()

        return download

    def main(self):
        for page in range(1,3):
            url=self.url.format(page)
            html=self.get_html(url)
            self.parse_page(html)
            #uniform:浮点数，爬取一个电影信息后sleep
            time.sleep(random.uniform(1,3))



if __name__=="__main__":
    start = time.time()
    spider=FilmSkySpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f' % (end - start))

