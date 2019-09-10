import redis,time,random
r=redis.Redis(host='127.0.0.1',port=6379,db=1)

while True:

    url=r.brpop('spider:urls',3)
    if url:
        print('正在抓取：',url[1].decode())
    else:
        print('抓取结束')
        break
