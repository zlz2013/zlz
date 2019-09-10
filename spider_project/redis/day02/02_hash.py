import redis
r=redis.Redis(host='127.0.0.1',port=6379,db=0)
r.hset('user2','name','zhangsan')
r.hset('user2','name','lisi')

username=r.hget('user2','name')
print('用户名是',username.decode())

dict1={
    'name':'zhangsan',
    'age':30,
    'gender':'M',
    'height':165,
    'password':123456
}
r.hmset('user3',dict1)

#获取
all_data=r.hgetall('user3')
print('all_data是',all_data)
h_keys=r.hkeys('user3')
print(h_keys)
h_vals=r.hvals('user3')
print(h_vals)



