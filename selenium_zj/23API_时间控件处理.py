from selenium import webdriver
import time
from selenium.webdriver.common import by               #导入by模块
from selenium.webdriver.support import expected_conditions #导入expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://hotel.meituan.com/beijing/')
time.sleep(3)           #强制等待时间
driver.maximize_window()
time.sleep(1)

# driver.find_element_by_xpath("//*[@name='checkIn' and @id='HD_CheckIn']").clear()  #普通时间控处理
# time.sleep(5)
# driver.find_element_by_xpath("//*[@name='checkIn' and @id='HD_CheckIn']").send_keys('2021-8-16')

#特殊的还未做
js = "document.getElementsByTagName('input')[5].removeAttribute('readonly')"  #列表
driver.execute_script(js)
driver.find_element_by_xpath("//*[@class='datepicker-group']/div[2]/div/input").clear()
time.sleep(5)
driver.find_element_by_xpath("//*[@class='datepicker-group']/div[2]/div/input").send_keys('2021-8-16')
