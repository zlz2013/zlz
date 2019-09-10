"""
死锁
"""
import time
import threading

#交易类
class Account:
    def __init__(self,_id,balance,lock):
        self.id=_id #用户
        self.balance=balance    #存款
        self.lock=lock  #锁

    #取钱
    def withdraw(self,amount):
        self.balance-=amount

    #存钱
    def deposit(self,amount):
        self.balance+=amount

    #查看余额
    def get_balance(self,amount):
        return self.balance


#创建账户
Tom=Account("Tom",5000,threading.Lock())
Alex=Account("Alex",8000,threading.Lock())

#转账函数
def transfer(from_,to,amount):
    if from_.lock.acquire():#锁自己账户
        from_.withdraw(amount)#自己账户减少
        time.sleep(0.5)#死锁
        if to.lock.acquire():#对方账户上锁
            to.deposit(amount)#对方账户增加
            to.lock.release()#对方账户解锁
        from_.lock.release()#自己账户解锁
    print("%s 给 %s 转账完成"%(from_.id,to.id))

t1=threading.Thread(target=transfer,args=(Tom,Alex,2000))
t2=threading.Thread(target=transfer,args=(Alex,Tom,2000))

t1.start()
t2.start()
t1.join()
t2.join()
