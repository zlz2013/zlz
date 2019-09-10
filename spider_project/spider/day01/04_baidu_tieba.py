from urllib import request,parse
import time,random

class BaiduSpider():
    def __init__(self):
        self.url='http://tieba.baidu.com/f?{}'
        self.headers={'user-agent':'mozilla/5.0'}

    #获取响应
    def get_page(self,url):
        req=request.Request(url=url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')
        return html

    #提取数据
    def parse_page(self):
        pass

    #保存数据
    def write_html(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)

    #主函数
    def main(self):
        baming = input('请输入吧名：')
        start = int(input('请输入起始页'))
        end = int(input('请输入终止页'))

        for i in range(start, end + 1):
            pn = (i - 1) * 50
            dict = {'kw': baming, 'pn': pn}
            params = parse.urlencode(dict)
            url=self.url.format(params)

            filename="{}-第{}页.html".format(baming,i)
            html=self.get_page(url)
            self.write_html(filename,html)
            print('第{}页爬取成功'.format(i))
            time.sleep(random.randint(1,3))

if __name__=='__main__':
    start=time.time()
    spider=BaiduSpider()
    spider.main()
    end=time.time()
    print('执行时间：%.2f'%(end-start))





