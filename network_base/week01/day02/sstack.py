"""
sstack.py   栈模型的顺序存储
重点代码

思路分析：
    1.列表即顺序存储，但是功能太多，不符合栈的模型
    2.利用列表，封装类，提供栈的接口方法
"""
#自定义异常类
class StackError(Exception):
    pass
#顺序栈类封装
class SStack:
    def __init__(self):
        #属性为空列表，这个列表就是栈的存储空间
        #列表最后一个元素为栈顶，
        self._elems=[]
    #判断栈是否为空
    def is_empty(self):
        return self._elems==[]
    #入栈
    def push(self,elem):
        self._elems.append(elem)
    #出栈
    def pop(self):
        # try:
        #     a=self._elems.pop()    #弹出列表最后一个
        # except:
        #     print("xxxx")
        # else:
        #     return a
        #self._elems为空则if语句为真
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop()

# if __name__=="__main__":
#     st=SStack() #初始化栈
#     st.push(10)
#     st.push(20)
#     st.push(30)
#     while not st.is_empty():
#         print(st.pop())


text="fsafdsa({fd[saf]ds}a)gdsagdsadsjafidshakghdsjkahgkdshanlg"
parens="{}[]()"
left_parens="{[("
opposite={
    "}":"{",
    "]":"[",
    ")":"("
}
st=SStack()
#负责提供遍历到的括号
def parent(text):
    i,text_len=0,len(text)
    while True:
        #循环遍历字符串，到结尾结束，遇到括号提供给ver
        while i<text_len and text[i] not in parens:
            i+=1
        if i >=text_len:
            return
        else:
            yield text[i],i
            i+=1
#字符是否匹配的验证工作
def ver():
    for pr, i in parent(text):
        if pr in left_parens:
            st.push((pr,i))
        elif st.is_empty() or st.pop()[0]!=opposite[pr]:
            print("Unmatching is found at %d for %s"%(i,pr))
            break
    #for循环正常结束
    else:
        if st.is_empty():
            print("All parentheses are matched")
        else:
            #剩下左括号
            p=st.pop()
            print("Unmatching is found at %d for %s" % (p[1], p[0]))
#主程序只负责做括号的验证
# for pr,i in parent(text):
#     print(pr,i)
ver()