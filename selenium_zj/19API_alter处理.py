from selenium import webdriver
import time
from selenium.webdriver.common import by               #导入by模块
from selenium.webdriver.support import expected_conditions #导入expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get('file:///D:\\25期\\自动化\\testAlert.html')
# time.sleep(3)           #强制等待时间
driver.maximize_window()
# time.sleep(1)
driver.execute_script('prom()')   #调用js

print(driver.switch_to.alert.text)     #alert 的文本信息
driver.switch_to.alert.send_keys('shabi')#alert 输入信息
driver.switch_to.alert.accept()       #alert 确认按钮
# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()      #alert 取消按钮
