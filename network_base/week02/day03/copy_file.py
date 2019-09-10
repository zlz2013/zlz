"""
 创建父子进程,复制一个文件,各自复制一半到新的文件中
"""
from multiprocessing import Process
import os,time

filename = "./1.txt"
size = os.path.getsize(filename)

# 父子进程使用fr会相互影响
fr = open(filename, 'rb')

def top():

  # fr = open(filename,'rb')
  fw = open('2.txt','wb')
  n = size // 2
  fw.write(fr.read(n))
  fr.close()
  fw.close()

def bot():

  # fr = open(filename, 'rb')
  fw = open('3.txt', 'wb')
  fr.seek(size//2,0)
  fw.write(fr.read())
  fr.close()
  fw.close()
p=Process(target=top)
p.start()
bot()
p.join()
# pid = os.fork()
#
# if pid < 0:
#   print("Error")
# elif pid == 0:
#
#   time.sleep(2)
#   top()  # 复制上半部分
# else:
#   time.sleep(1)
#   bot()  # 下半部分


