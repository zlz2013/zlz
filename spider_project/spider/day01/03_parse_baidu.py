#将网页请求保存到本地

from urllib import request,parse

#拼接URL地址
def get_url(word):

    # url='http://www.baidu.com/s?{}'
    # params=parse.urlencode({'wd':word})
    url='http://www.baidu.com/s?wd={}'
    params=parse.quote(word)
    url=url.format(params)

    return url

#发请求，保存到本地文件
def request_url(url,filename):
    headers={'User-Agent': 'Mozilla/5.0'}
    req=request.Request(url,headers=headers)
    res=request.urlopen(req)
    html=res.read().decode('utf-8')
    print(html)
    #保存到本地
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)


if __name__=="__main__":
    word=input('请输入搜索的内容：')
    # dict={'wd':word}
    url=get_url(word)
    print(url)
    filename="{}.html".format(word)
    request_url(url,filename)