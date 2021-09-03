# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.amap.com/')   #ip地址
# driver.find_element_by_class_name('searchbox').click()  #class 不能有空格


# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.amap.com/')   #ip地址
# driver.find_element_by_class_name('amap-info').click()  #class 不能有空格

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://www.iqiyi.com/')   #ip地址
# driver.find_element_by_class_name('header-sideItemCon').click()  #class 不能有空格

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.iqiyi.com/') #ip地址
driver.maximize_window()
driver.find_element_by_class_name('logo-svg-nonIndex').click()  #class 不能有空格