import redis,pymysql

#(mysql)update数据后，同步到redis缓存
def update_mysql(username,new_age):
    #连接数据库
    db=pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='123456',
        charset='utf8',
        database='zlz'
    )
    cursor=db.cursor()
    select="update user1 set age=%s where username=%s"
    try:
        #更新之后返回值为code：0/1
        code=cursor.execute(select,[new_age,username])
        print(code)
        db.commit()
        if code:
            return True
        else:
            return False
    except Exception as e:
        db.rollback()
        print("error",e)
    db.close()

def update_redis(username,new_age):
    r=redis.Redis(host='127.0.0.1',port=6379,db=2)

    r.hset(username,'age',new_age)
    print('已同步到redis缓存')
    r.expire(username,60)
    print(r.hget(username,'age'))



if __name__=='__main__':
    username=input('请输入用户名:')
    new_age=input('请输入新年龄:')
    if update_mysql(username,new_age):
        update_redis(username,new_age)
    else:
        print('数据库不存在该用户，同步失败')