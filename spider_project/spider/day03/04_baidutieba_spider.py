import requests
from lxml import etree
import random,time
from model_tool.useragents import ua_list
from urllib import parse

class BaiduImageSpider():
    def __init__(self):
        self.url='http://tieba.baidu.com/f?kw={}&pn={}'

    #获取html功能函数
    def get_html(self,url):
        headers={'user-agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        html=requests.get(url=url,headers=headers).content.decode('utf-8','ignore')
        return html


    #解析html功能函数
    def xpath_func(self,html,xpath_bds):
        parse_html=etree.HTML(html)
        r_list=parse_html.xpath(xpath_bds)
        return r_list


    #解析函数-实现最终图片抓取
    def parse_html(self,one_url):
        html=self.get_html(one_url)
        #准备提取帖子连接:xpath_list['/p/23132','','']
        xpath_bds='//div[@class="t_con cleafix"]/div/div/div/a/@href'
        r_list=self.xpath_func(html,xpath_bds)
        print(r_list)
        for r in r_list:
            #拼接帖子的URL地址
            t_url='http://tieba.baidu.com'+r
            #把帖子中所有图片保存到本地
            self.get_image(t_url)
            time.sleep(random.uniform(1,2))

    def get_image(self,t_url):
        html=self.get_html(t_url)
        xpath_img='//img[@class="BDE_Image"]/@src'
        img_list=self.xpath_func(html,xpath_img)

        for img in img_list:
            html_byte=requests.get(url=img,headers={'user-agent':random.choice(ua_list)}).content
            self.save_img(html_byte,img)

    def save_img(self,html_byte,img):
        filename=img[-10:]
        with open('./img/'+filename,'wb') as f:
            f.write(html_byte)
            print('%s下载成功'%filename)



    #主函数
    def main(self):
        name=input('请输入贴吧名')
        begin=int(input('请输入起始页'))
        end=int(input('请输入终止页'))
        #对贴吧名进行编码
        kw=parse.quote(name)
        for page in range(begin,end+1):
            pn=(page-1)*50
            url=self.url.format(kw,pn)
            #调用主线函数
            self.parse_html(url)


if __name__=='__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = BaiduImageSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end - start))