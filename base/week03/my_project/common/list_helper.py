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
    @staticmethod
    def find_count(list_target, fun):
        """
            获取满足条件的元素的数量
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """
        count=0
        for i in list_target:
            if fun(i):
                count+=1
        return count

    @staticmethod
    def find_sum(list_target, fun):
        """
            获取满足条件的元素的总和
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """
        sum=0
        for i in list_target:
            sum+=fun(i)
        return sum

    @staticmethod
    def find_max(list_target, fun):
        """
            获取满足条件的最大元素
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """
        my_max=fun(list_target[0])
        for i in range(1,len(list_target)):
            if my_max<fun(list_target[i]):
                my_max=fun(list_target[i])
        return my_max

    @staticmethod
    def find_min(list_target, fun):
        """
            获取满足条件的最小元素
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """
        my_min = fun(list_target[0])
        for i in range(1, len(list_target)):
            if my_min > fun(list_target[i]):
                my_min = fun(list_target[i])
        return my_min

    @staticmethod
    def find_list(list_target, fun):
        """
            将满足条件的元素加入列表
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """
        list_target01=[]
        for i in list_target:
            list_target01.append(fun(i))
        return list_target01

    @staticmethod
    def find_sheng(list_target, fun):
        """
            将满足条件的元素加入列表,并升序显示
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """

        for item in range(len(list_target)-1):
            for c in range(item+1,len(list_target)):
                if fun(list_target[item])>fun(list_target[c]):
                    list_target[item],list_target[c]=list_target[c],list_target[item]


    @staticmethod
    def find_jiang(list_target, fun):
        """
            将满足条件的元素加入列表，并降序显示
        :param list_target: 目标列表
        :param fun: 查找方法
        :return: 返回列表中的元素或对象，生成器对象
        """
        list_target01 = []
        for i in list_target:
            list_target01.append(fun(i))
        for item in range(len(list_target01) - 1):
            for c in range(item, len(list_target01)):
                if list_target01[item] < list_target01[c]:
                    list_target01[item], list_target01[c] = list_target01[c], list_target01[item]
        return list_target01