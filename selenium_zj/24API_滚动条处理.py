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

js = 'var q=document.documentElement.scrollTop=10000'#默认值10000
driver.execute_script(js)  #滚动到底部
time.sleep(5)
js = 'var q=document.documentElement.scrollTop=0'#默认值10000
driver.execute_script(js)   #滚动到顶部
driver.execute_script('window.scrollTo(0,300)')   #滚动部分
time.sleep(5)
driver.execute_script('window.scrollBy(0,-100)')  #相对滚动