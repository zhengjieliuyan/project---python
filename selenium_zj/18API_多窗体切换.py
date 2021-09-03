from selenium import webdriver
import time
from selenium.webdriver.common import by               #导入by模块
from selenium.webdriver.support import expected_conditions #导入expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)           #强制等待时间
driver.maximize_window()
time.sleep(1)
print(driver.window_handles)          #打开所有窗体的句柄
driver.find_element_by_xpath("//a[@class='header'][3]").click()
time.sleep(3)
print(driver.window_handles)
print(driver.current_window_handle)     #打开当前窗体的句柄
driver.switch_to.window(driver.window_handles[1])  #切换窗体的句柄
print(driver.current_window_handle)
driver.close()
