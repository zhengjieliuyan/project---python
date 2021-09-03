from selenium import webdriver
import time
from selenium.webdriver.common import by               #导入by模块
from selenium.webdriver.support import expected_conditions #导入expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
# time.sleep(3)           #强制等待时间
driver.maximize_window()
# time.sleep(1)

# driver.implicitly_wait(10)   #隐式等待时间  全局等待变量
#
# driver.find_element_by_xpath("//*[@class='but1']").clear()
# driver.find_element_by_xpath("//*[@class='but1']").send_keys('小宁')
# driver.find_element_by_xpath("//*[@class='but2']").click()


ad = WebDriverWait(driver,20,0.5).until(expected_conditions.presence_of_element_located((by.By.XPATH,"//*[@class='but2']")))
ad.click()
time.sleep(5)
driver.quit()