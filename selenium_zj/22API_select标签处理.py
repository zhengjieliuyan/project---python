from selenium import webdriver
import time
from selenium.webdriver.common import by               #导入by模块
from selenium.webdriver.support import expected_conditions #导入expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.ctrip.com/')
time.sleep(3)           #强制等待时间
driver.maximize_window()
time.sleep(1)
# Select(driver.find_element_by_xpath("//*[@id='searchHotelLevelSelect']")).select_by_visible_text('五星级/豪华')
Select(driver.find_element_by_xpath("//*[@id='searchHotelLevelSelect']")).select_by_index('1')
# Select(driver.find_element_by_xpath("//*[@id='searchHotelLevelSelect']")).select_by_value('5')

