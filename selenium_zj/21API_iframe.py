from selenium import webdriver
import time
from selenium.webdriver.common import by               #导入by模块
from selenium.webdriver.support import expected_conditions #导入expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
time.sleep(3)           #强制等待时间
driver.maximize_window()
time.sleep(3)

# driver.switch_to.frame('login_frame')         #通过控件属性来定位
# driver.find_element_by_xpath("//*[@class='inputstyle']").send_keys('13435634524')

driver.switch_to.frame(driver.find_element_by_xpath("//*[@class='xm_login_card_qq']/iframe"))
driver.find_element_by_xpath("//*[@class='inputstyle']").send_keys('13435634524')


