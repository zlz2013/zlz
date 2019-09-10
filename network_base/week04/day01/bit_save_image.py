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

# #存储文件
# with open('1.jpeg','rb') as fd:
#     data=fd.read()
# try:
#     sql="insert into Image (filename,data) \
#                         values('1.jpeg',%s);"
#     cur.execute(sql,[data])
#
# #将写操作提交到数据库
#     db.commit()
# except:
#     db.rollback()

#获取图片
sql='select * from Image where filename="1.jpeg"'
cur.execute(sql)
img=cur.fetchone()
with open(img[1],'wb') as f:
    f.write(img[2])
#关闭数据库
cur.close()
db.close()