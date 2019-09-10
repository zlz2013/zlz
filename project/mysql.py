from hashlib import md5
pwd = input('please input your password:')
#1.创建sha1加密对象
s = md5()
#2.进行加密，参数一定为bytes数据类型
s.update(pwd.encode())
#encode :字符串-》bytes
#3.获取16进制的加密结果
pwd = s.hexdigest()
print(pwd)
#decode: bytes->字符串

