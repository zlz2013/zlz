import time

from selenium import webdriver

#创建浏览器对象
browser=webdriver.Chrome()
browser.get('http://www.baidu.com/')
#获取快照
html=browser.page_source
print(html.find('kw'))
browser.save_screenshot('baidu.jpg')
time.sleep(10)

#关闭浏览器
browser.quit()
