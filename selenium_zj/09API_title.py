from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
title = driver.title   #获取文案文本信息
print(title)
driver.find_element_by_css_selector('.schhot>a:nth-child(4)').click()
title = driver.title   #获取文案文本信息
print(title)