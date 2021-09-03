
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# driver.maximize_window()
# # time.sleep(2)
#
# driver.find_element_by_name('nav-bar-mname').click()

from selenium import webdriver

driver = webdriver.Chrome()             #把webdriver.Chrome赋值给一个变量
driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
driver.maximize_window()
# time.sleep(2)
driver.find_element_by_name('checkOut').clear()    #清除定位控件的里面的内容
driver.find_element_by_name('checkOut').send_keys('2021-8-19')  #定位控件并传一个参数