from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
a = driver.find_element_by_xpath("//input[@class='but2']").size   #查看属性
print(a,type(a))
print(a['height'])
b = driver.find_element_by_xpath("//input[@class='but2']").get_attribute('value')  #查看控件文本
print(b)
c = driver.find_element_by_xpath("//a[@href='http://101.133.169.100/yuns/index.php/goods?key=全场一员']").text
print(c)        #文本控件需要赋值于一个变量
d = driver.find_element_by_xpath("//a[text()='联系客服']").is_displayed()
print(d)
# def add():
#     x =2
#     y = 3
#     z = x+y
#     return x
# b = add()
