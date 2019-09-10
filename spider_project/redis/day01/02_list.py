import redis
r=redis.Redis(host='176.47.7.235',port=6379,db=0,password=None)


# r.lpush('pylist','pybase','socket','pyweb')
print(r.lrange('pylist',0,-1))

#linsert pylist before/after pyweb spider
# r.linsert('pylist','after','pyweb','spider')
print(r.lrange('pylist',0,-1))

print(r.llen('pylist'))
# r.lpop('pylist')
# r.rpop('pylist')
r.lrem('pylist',0,'pyweb')
print(r.lrange('pylist',0,-1))

# while True:
#     res=r.brpop('pylist',3)
#     if res:
#         print(res)
#     else:
#         break

print(r.ltrim('pylist',0,3))
r.lset('pylist',3,'pyweb')
print(r.lrange('pylist',0,-1))