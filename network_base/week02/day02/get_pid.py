"""
获取PID
"""
import os,time
pid=os.fork()
if pid<0:
    print("创建进程失败")
elif pid==0:

    time.sleep(2)
    print("子进程")
    print("child PID=",os.getpid())
    print("parent PID=",os.getppid())
else:
    # os._exit(0)
    # time.sleep(1)
    print("父进程")
    print("child PID=", pid)
    print("parent PID=", os.getpid())
    print("  PID=", os.getppid())
print("fork测试结束")

