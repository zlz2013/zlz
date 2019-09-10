import time
#获得时间戳  秒
# print(time.time())
#获得时间元组
# print(time.localtime(time.time()))
#获得时间元组中第一项
# print(time.localtime(time.time())[0])
#遍历时间元组中的项
# for item in time.localtime(time.time()):
#     print(item)

# tuple_time=time.localtime(time.time())
# print(tuple_time)
#时间元组转换成特定格式时间
# print(time.strftime("%Y/%m/%d %H:%M:%S",tuple_time))
# print(time.strftime("%y/%m/%d %H:%M:%S",tuple_time))
#根据时间获得对应的时间元组
# print(time.strptime("2019-05-21 09:39:25","%Y-%m-%d %H:%M:%S"))
#时间元组转化为时间戳（秒）
# print(time.mktime(tuple_time))

#输入年月日获得星期
# def week(year,month,day):
#     time01=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
#     dict_week={
#         0:"星期一",
#         1:"星期二",
#         2:"星期三",
#         3:"星期四",
#         4:"星期五",
#         5:"星期六",
#         6:"星期日",
#     }
#     return dict_week[time01[6]]
# print(week(2019,5,21))

#活了多少天
# def week(year,month,day):
#     time01=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
#     time02=time.time()-time.mktime(time01)
#     return time02
# print(week(1992,1,24))
# print(week(1992,1,24)/60/60//24)

