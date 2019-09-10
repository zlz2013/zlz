def count(x,y):
    c=0
    while c<700000:
        c+=1
        x+=1
        y+=1

def io():
    wrire()
    read()

def write():
    f=open("test","w")
    for i in range(1800000):
        f.write("Hello world\n")
