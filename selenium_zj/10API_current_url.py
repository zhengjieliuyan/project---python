from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
url = driver.current_url   #获取当前页面的地址
print(url)
driver.find_element_by_css_selector('.schhot>a:nth-child(4)').click()
url = driver.current_url   #获取当前页面的地址  一个页面就是一个地址
print(url)
