from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys  #导入模块下的一个类
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
driver.find_element_by_xpath("//*[@class='but1']").send_keys('周剑')
driver.find_element_by_xpath("//*[@class='but1']").send_keys(Keys.BACK_SPACE)
