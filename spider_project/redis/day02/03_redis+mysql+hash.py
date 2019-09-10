import redis,pymysql

r=redis.Redis(host='127.0.0.1',port=6379,db=2)

#1.先到redis中查询
#2.redis中没有，到MySQL中查询，缓存到redis中（设置过期时间）
#3.在查询一次
username=input('请输入用户名:')
res=r.hgetall(username)
if res:
    print("redis中找到：",res)

else:
    db=pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456',
        charset='utf8',
        database='zlz'
    )
    cursor=db.cursor()
    select='select username,password,gender,age from user1 where username=%s'
    cursor.execute(select,[username])
    userinfo=cursor.fetchall()
    print(userinfo)
    if not userinfo:
        print("mysql中用户信息不存在")
    else:
        dict={
            'username':userinfo[0][0],
            'password':userinfo[0][1],
            'gender':userinfo[0][2],
            'age':userinfo[0][3]
        }
        r.hmset(username,dict)
        r.expire(username,60*5)
        print('redis缓存成功')

