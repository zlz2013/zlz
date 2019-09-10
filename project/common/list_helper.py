class ListHelper:
    """
    列表助手：定义列表的常用操作
    """
    @staticmethod
    def find(list_target, fun):
        """
            在列表中根据制定条件查找所有元素
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """
        for i in list_target:
            if fun(i):
                yield i