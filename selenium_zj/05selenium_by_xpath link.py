# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php/')
# sleep(3)
# driver.maximize_window()
#
# driver.find_element_by_xpath("//a[text()='鞋子包包']").click()      #a标签下的text文本定位


# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php/')
# sleep(3)
# driver.maximize_window()
#
# driver.find_element_by_xpath("//div[@class='logo_bar']/div/div/div/a[1]").click()        #父找子的相对路径


# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php/')
# sleep(3)
# driver.maximize_window()
#
# driver.find_element_by_xpath("//a[text()='家装节']/../../div[1]/form/input[1]").click()
# sleep(3)
# driver.find_element_by_xpath("//a[text()='家装节']/../../div[1]/form/input[1]").send_keys('周剑')

# from selenium import webdriver
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php/')
# sleep(3)
# driver.maximize_window()
#
# driver.find_element_by_xpath("//div[@class='schhot']/a[text()='运动男鞋']").click()

# driver.find_element_by_xpath("//a[text()='家装节']/../../div[1]/form/input[1]").send_keys('周剑')

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php/')
sleep(3)
driver.maximize_window()

driver.find_element_by_xpath("//div[@class='schhot']/a[text()='运动男鞋']").click()







