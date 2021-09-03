from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
driver.find_element_by_css_selector('.schhot>a:nth-child(4)').click()
time.sleep(2)
driver.refresh()   #一个窗口刷新
time.sleep(2)
driver.back()        #一个窗口后退
time.sleep(2)
driver.forward()           #一个窗口前进
time.sleep(2)