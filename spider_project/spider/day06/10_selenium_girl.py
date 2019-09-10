from selenium import webdriver

#1.创建浏览器对象-已经打开了浏览器
browser=webdriver.Chrome()
#2.输入地址：http://www.baidu.com/
browser.get('http://www.baidu.com/')
#3.找到搜索框节点，向这个搜索框节点发送文字，赵丽颖
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
#4.找到百度一下按钮，点击下去
browser.find_element_by_xpath('//*[@id="su"]').click()