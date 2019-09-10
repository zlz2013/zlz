# 程序结构
import time
class xxxSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        pass

    def get_html(self):
        # 获取响应内容函数,使用随机User-Agent
        pass

    def parse_html(self):
        # 使用正则表达式来解析页面,提取数据
        pass

    def write_html(self):
        # 将提取的数据按要求保存,csv、MySQL数据库等
        pass

    def main(self):
        # 主函数,用来控制整体逻辑
        pass

if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = xxxSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))