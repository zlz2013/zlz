import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=2)
r.sadd('user1','peiqi','qiaozhi','danni')
r.sadd('user2','peiqi','qiaozhi','wangweichao')
res=r.sinter('user1','user2')
res2=r.sdiff('user1','user2')
res3=r.sunion('user1','user2')
print(res2)
print(res3)
print(res)
focus=set()
for i in res:
    focus.add(i.decode())
print(focus)