import getpass#输入隐藏显示
import hashlib#转换加密

#输入隐藏
pwd=getpass.getpass("pw:")
print(pwd)

#加密处理,生成hash对象
# hash=hashlib.md5()#通过对象

#算法加盐
hash=hashlib.md5("!@#".encode())
hash.update(pwd.encode())#加密算法
pwd=hash.hexdigest()#提取加密后的密码
print(pwd)
#二次加密
# hash.update(pwd.encode())#加密算法
# pwd=hash.hexdigest()#提取加密后的密码
# print(pwd)