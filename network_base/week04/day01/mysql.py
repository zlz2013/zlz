"""
pymysql 操作数据库基本流程
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
sql="insert into test1 (name,age,sex,score) \
                        values('lily',14,'w',79.5);"
cur.execute(sql)

#将写操作提交到数据库
db.commit()

#关闭数据库
cur.close()
db.close()