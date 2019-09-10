from selenium import webdriver
from ydmapi import get_result
from PIL import Image

class AttackYdm():
    def __init__(self):
        self.browser=webdriver.Chrome()


    #1.获取网站首页截图
    def get_index_shot(self):
        self.browser.get('http://www.yundama.com')
        self.browser.save_screenshot('index.png')


    #2.从首页截图中截取验证码图片
    def get_caphe(self):
        xpath_bds='//*[@id="verifyImg"]'
        #定位验证码元素的位置左上角（x,y）坐标
        location=self.browser.find_element_by_xpath(xpath_bds).location
        #获取大小（宽度和高度）
        size=self.browser.find_element_by_xpath(xpath_bds).size
        #计算四个坐标，左上角和右下角（x,y）
        left_x=location['x']
        left_y=location['y']
        right_x=left_x+size['width']
        right_y=left_y+size['height']

        img=Image.open('index.png').crop((left_x,left_y,right_x,right_y))
        print(img)
        img.save('ydm.png')




    #3.在线识别验证码
    def get_code(self):
        res = get_result('ydm.png')
        return res

    def main(self):
        self.get_index_shot()
        self.get_caphe()
        res=self.get_code()
        print(res)
if __name__=='__main__':
    spider=AttackYdm()
    spider.main()