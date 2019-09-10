# machine_checker.py
# 设备故障判断，对设备上报的数据进行查询、分析
# 如果某个设备一定时间未报告状态，或关键数据超标
# 则插入一笔数据到设备故障表
from db_coffee_dao import *
from db_helper import *
from db_conf import *
import time

def main():
    db_helper = DBHelper()  #实例化一个数据访问对象
    coffeeDao = CoffeeDao(db_helper)

    while True:
        # do_check_last_send_time(coffeeDao)  # 检查设备最后发送数据时间
        do_check_boiler_tmer(coffeeDao)
        time.sleep(1)

#检查每台设备的关键参数，如果参数超过该型号运行的最大值
#则在设备报警表中，插入一条报警数据
def do_check_boiler_tmer(coffeeDao):
    #查询每台设备最后发送的一笔数据，根据设备编号，取得类型信息，
    # 用每笔数据中的锅炉温度和类型信息表的锅炉温度比较，如果超过类型信息表的值，则报警
    result=coffeeDao.get_last_eqinfo()  #查询每台机器最后发送的一笔数据
    for row in result:
        machine_id=row[1]   #设备标号字段
        boiler_tempr=row[4] #锅炉温度字段
        eqtype=coffeeDao.get_categray_info_by_machine_id(machine_id)    #获取设备型号信息
        if len(eqtype)>0:   #查到该设备型号信息
            work_tempr=float(eqtype[0][10]) #锅炉最大工作温度
            boiler_tempr=float(boiler_tempr)    #实际工作温度为浮点数
            if boiler_tempr>work_tempr: #实际温度大于最高温度
                alert_msg="%d号设备温度超标"%machine_id
                print(alert_msg)
                #在告警表插入一笔数据
                coffeeDao.add_machine_warnings(machine_id,alert_msg)


# 查询所有设备最后发送数据时间到当前时间点的事件间隔，并判断故障
def do_check_last_send_time(coffeeDao):
    result = coffeeDao.query_machine_last_send()
    for i in result:
        machine_id = int(i[0])  # 设备ID
        diff_time = i[1]  # 到当前时间点时间差
        alert_msg = ""
        is_broken = False 

        if not diff_time:
            is_broken = True
            alert_msg = "编号%d的咖啡机没有上报状态，可能存在故障" % machine_id
        elif diff_time >= machine_max_interval:
            is_broken = True
            alert_msg = "编号%d的咖啡机最后一次上报状态已经%d秒，可能存在故障" % (machine_id, diff_time)

        if is_broken:
            result = coffeeDao.add_machine_warnings(machine_id, alert_msg)
             

if __name__ == "__main__":
    main()

