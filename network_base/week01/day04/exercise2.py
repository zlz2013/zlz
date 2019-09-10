"""
3. 向一个文件写入日志, 写入格式:
     1.  2019-1-1 12:12:12
     2.  2019-1-1 12:12:13
     3.  2019-1-1 12:12:24
    要求每隔1秒写入一次,每条时间占一行.程序死循环,crtl-c退出.
    如果程序退出重新启动时内容能跟上次内容衔接(序列号)
"""
import time
# print(time.ctime())
# while True:
#     # 获得时间戳  秒
#     time01 = time.time()
#     # 获得时间元组
#     time02 = time.localtime(time.time())
#     # 时间元组转换成特定格式时间
#     time03 = time.strftime("%Y/%m/%d %H:%M:%S\n", time02)
#     f=open("tetst","a")
#     fd = open("tetst")
#     list01 = fd.readlines()
#     count = len(list01)+1
#     s="%d. %s"%(count,time03)
#     f.write(s)
#     f.flush()
#     fd.flush()
#     # f.write(str(count))
#     # f.write(". ")
#     # f.write(time03)
#     time.sleep(1)
#     fd1=open("tetst","r")
#     f.close()
#     fd.close()

n=0
fr=open("tetst","a+")
fr.seek(0,0)
for i in fr:
    n+=1
while True:
    n += 1
    time.sleep(1)
    data=time.ctime()
    s = "%d. %s\n" % (n, data)
    fr.write(s)
    fr.flush()

