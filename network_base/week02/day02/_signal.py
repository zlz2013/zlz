"""
信号方法处理僵尸
"""
import signal,os
#子进程退出时，父进程会忽略，此时子进程由系统自动处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
pid=os.fork()
if pid<0:
    print("创建进程失败")
elif pid==0:
    # time.sleep(2)
    print("子进程")
    print("child PID=",os.getpid())
    print("parent PID=",os.getppid())
else:
    # p,status=os.wait()
    print("退出的子进程PID号：",)
    print("退出的子进程状态：",)
    while True:
        pass