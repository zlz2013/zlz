"""
pymysql 数据库写操作(增删改)
"""

import pymysql

#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   passwd='123456',
                   database='zlz',
                   charset='utf8'
                   )

#获取游标(用于进行数据操作的对象,承载操作结果)
cur=db.cursor()

#执行SQL语句
try:
    #插入数据
    # name=input('name:')
    # age=int(input('age:'))
    # sex=input('sex:')
    # score=float(input('score:'))
    # sql="insert into test1 (name,age,sex,score) \
    #                 values(%s,%s,%s,%s);"
    # cur.execute(sql,[name,age,sex,score])
    # db.commit()

    #修改操作
    # sql='update test1 set age=33 where name="张三";'
    # cur.execute(sql)
    # db.commit()

    #删除操作
    sql='delete from test1 where score>100'
    cur.execute(sql)
    db.commit()

except Exception as e:
    db.rollback()#退回到commit之前的状态
    print(e)



#关闭数据库
cur.close()
db.close()