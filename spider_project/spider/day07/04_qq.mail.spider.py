from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://mail.qq.com/cgi-bin/loginpage')

#找iframe子框架，并切换到此框架
login_frame=browser.find_element_by_id('login_frame')
browser.switch_to.frame(login_frame)

#qq+密码+登录

browser.find_element_by_id('u').send_keys('229165631@qq.com')
browser.find_element_by_id('p').send_keys('')
browser.find_element_by_id('login_button').click()