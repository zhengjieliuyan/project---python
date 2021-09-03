from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
driver.find_element_by_css_selector('.schhot>a:nth-child(4)').click()  #点击事件
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys('周剑')#输入时间
time.sleep(4)
driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").clear() #清空


# def add():
#     x =2
#     y = 3
#     z = x+y
#     return x
# b = add()
# print(b,type(b))