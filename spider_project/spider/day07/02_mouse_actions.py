#导入鼠标事件类
from selenium import webdriver
from selenium.webdriver import ActionChains

browser=webdriver.Chrome()
browser.get('http://www.baidu.com/')

#找到设置节点
# browser.find_element_by_id('kw').send_keys('赵丽颖')
# browser.find_element_by_id('su').click()

actions=ActionChains(browser)
element=browser.find_elements_by_name('tj_settingicon')[1]
actions.move_to_element(element).perform()

#找到高级设置，并点击
browser.find_element_by_link_text('高级搜索').click()
