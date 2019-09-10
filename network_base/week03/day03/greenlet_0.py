"""
协程运行形态示例
"""


from greenlet import greenlet

def test1():
    print("执行test1")
    # gr2.switch()
    print("结束test1")
    # gr2.switch()


def test2():
    print("执行test2")
    # gr1.switch()
    print("结束test2")

gr1=greenlet(test1)
gr2=greenlet(test2)
# gr1.switch()
# gr2.switch()

