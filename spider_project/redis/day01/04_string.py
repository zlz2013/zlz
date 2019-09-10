import redis,time,random
r=redis.Redis(host='127.0.0.1',port=6379,db=1)


r.set('pystr','python')
print(r.get('pystr').decode())

r.mset({'username':'小泽','password':123456})
print(r.mget('username','password'))
print(r.strlen('username'))
r.set('age','25')
r.incrby('age',10)
r.incr('age')
r.incrbyfloat('age',6.66)
print(r.get('age'))