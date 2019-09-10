"""
pymysql 字典
"""

import pymysql

#链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   passwd='123456',
                   database='dict',
                   charset='utf8'
                   )

#获取游标(用于进行数据操作的对象,承载操作结果)
cur=db.cursor()

#执行SQL语句
# try:
#     #插入数据
f=open('dict1.txt','r')
for i in f:
    a=i.split(' ')[0]
    b = i.split(' ')[1:]
    c = ' '.join(b)
    d = c.strip()
    print(d.decode())
#         sql="insert into words (name,mean) \
#                     values(%s,%s);"
#         cur.execute(sql,[a,d])
#     db.commit()
#     f.close()
# except Exception as e:
#     db.rollback()#退回到commit之前的状态
#     print(e)



#关闭数据库
cur.close()
db.close()