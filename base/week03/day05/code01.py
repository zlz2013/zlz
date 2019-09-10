def chmod(fun):
    def fun01(*args,**kwargs):
        print("验证权限")
        if True:
            return fun(*args,**kwargs)
        else:
            print("验证失败")
    return fun01
@chmod
def enter_background(a):
    print(a,"进入后台系统")

@chmod
def delete_order():
    print("删除订单")

delete_order()
enter_background("hello")

