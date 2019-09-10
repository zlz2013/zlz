import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password=123456)

day01_dict={
    'huawei':5000,
    'oppo':4000,
    'iphone':3000
}

day02_dict={
    'huawei':5200,
    'oppo':4200,
    'iphone':3200
}

day03_dict={
    'huawei':5500,
    'oppo':4500,
    'iphone':3500
}

r.zadd('mobile-001',day01_dict)
r.zadd('mobile-002',day02_dict)
r.zadd('mobile-003',day03_dict)

r.zunionstore('union-3',('mobile-001','mobile-002','mobile-003'),aggregate='max')

rlist=r.zrange('union-3',0,-1,withscores=True,desc=True)
print(rlist)
c=1
for i in rlist:
    print('第{}名：{}，销量为:{}'.format(c,i[0].decode(),int(i[1])))
    c+=1