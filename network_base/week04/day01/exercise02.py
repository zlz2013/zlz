"""
pymysql 字典
"""

import pymysql
import re

f=open('dict.txt','r')
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
    sql = "insert into words (word,mean) \
                        values(%s,%s);"
    for i in f:
        #获取Word和mean
        tup=re.findall(r'(\S+)\s+(.*)',i)[0]
        cur.execute(sql,tup)
    db.commit()
    f.close()
except Exception as e:
    db.rollback()#退回到commit之前的状态
    print(e)
#关闭数据库
cur.close()
db.close()