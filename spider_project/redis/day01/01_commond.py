import redis
r=redis.Redis(host='176.47.7.235',port=6379,db=0,password=None)
r_list=r.keys('*')
for k in r_list:
    print(k.decode())
print()
print(r.type('spider:urls').decode())
print()
print(r.exists('spider:urls'))
print()
r.delete("list")
r.delete("spider:urls")