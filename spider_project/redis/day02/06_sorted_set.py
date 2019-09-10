import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=3)
dict1={
    'zhouzhiruo':777,
    'zhangwuji':999,
    'zhaomin':888
}
r.zadd('salary',dict1)
s=r.zrange('salary',0,-1,withscores=True,desc=True)
print(s)