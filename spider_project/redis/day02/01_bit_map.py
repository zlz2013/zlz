import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0)

r.setbit('user1',4,1)
r.setbit('user1',199,1)
r.setbit('user2',99,1)
r.setbit('user2',299,1)

for i in range(1,366,2):
    r.setbit('user3',i,1)

for i in range(1,366,3):
    r.setbit('user4',i,1)

user_list=r.keys('user*')
print(user_list)
active_user=[]
noacrive_user=[]
for user in user_list:
    count=r.bitcount(user)

    if count>=100:
        active_user.append((user.decode(),count))
    else:
        noacrive_user.append((user.decode(),count))

for active in active_user:
    print('活跃用户：',active)

for active in noacrive_user:
    print('不活跃用户：',active)