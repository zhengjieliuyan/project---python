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
driver.get_screenshot_as_file('d:/1.png')      #保存路径使用左斜杠  保存路径+图片名字和格式

driver.find_element_by_xpath("//*[@class='but2']").click()
time.sleep(3)
driver.get_screenshot_as_file('d:/2.png')


