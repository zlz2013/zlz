import pymongo

#1.连接对象
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)

#2.库对象
db=conn['maoyandb']
# db=conn.maoyandb  ->有弊端，不建议使用

#3.集合对象
myset=db['filmtab']


#4.插入数据库
myset.insert_one({'name':'赵敏'})