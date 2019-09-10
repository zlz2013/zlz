"""
mysql 数据库读操作
select语句
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
sql="select score from test1 where name='张三';"
cur.execute(sql)#执行查询操作之后，cur便会拥有查询结果

#获取一个查询结果
one_row=cur.fetchone()
print(one_row)

#获取多个查询结果
# two_row=cur.fetchmany(2)
# print(two_row)

#获取全部查询结果
# all_row=cur.fetchall()
# print(all_row)

# #将写操作提交到数据库
# db.commit()

#关闭数据库
cur.close()
db.close()

