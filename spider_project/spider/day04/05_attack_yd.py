import requests
import time,random
from hashlib import md5


class YdSpider():
    def __init__(self):
        self.url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "238",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=719627021@10.169.0.83; JSESSIONID=aaakMEEqIJOxOazJkikYw; OUTFOX_SEARCH_USER_ID_NCOO=1747473194.4334164; ___rl__test__cookies=1565685533880",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Pragma": "no-cache",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

    #获取
    def get_salt_sign_ts(self,word):

        ts=str(int(time.time()))
        salt=ts+str(random.randint(0,9))
        string="fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s=md5()
        s.update(string.encode())
        sign=s.hexdigest()
        data = {
            'i': word,
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
        return data
    #主函数
    def attack_yd(self,word):
        #1.先拿到salt,sign,ts
        data=self.get_salt_sign_ts(word)

        #2.定义form表单数据为字典， data={}
        #3.直接发请求：requests.post(url,data=data,headers=headers)
        json_html=requests.post(url=self.url,data=data,headers=self.headers).json()
        #4.获取响应内容
        res=json_html['translateResult'][0][0]['tgt']
        return res

    def main(self,word):
        #输入翻译单词
        return self.attack_yd(word)

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    word=input('请输入你要翻译的单词:')
    spider = YdSpider()
    print(spider.main(word))
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))