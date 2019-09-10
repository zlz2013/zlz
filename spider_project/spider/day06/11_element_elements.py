from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.qiushibaike.com/text/')

#单元素查找
div=browser.find_element_by_class_name('content')
print(div.text)

#多元素查找
divs=browser.find_elements_by_class_name('content')
for i in divs:
    print('*'*50)
    print(i.text)
    print('*'*50)