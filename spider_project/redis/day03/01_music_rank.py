import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0)

r.zadd('ranking',{'song1':1,'song2':1,'song3':1,'song4':1})
r.zadd('ranking',{'song5':1,'song6':1,'song7':1,'song8':1})
r.zadd('ranking',{'song9':1,'song10':1,'song11':1,'song12':1})

#指定成员增加分值
r.zincrby('ranking',50,'song3')
r.zincrby('ranking',70,'song5')
r.zincrby('ranking',90,'song7')

rlist=r.zrevrange('ranking',0,2,withscores=True)
print(rlist)

c=1
for i in rlist:
    print('第%d名：%s，播放次数:%s'%(c,i[0].decode(),int(i[1])))
    c+=1