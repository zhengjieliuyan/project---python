# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php/')
# time.sleep(3)
# driver.maximize_window()
# driver.find_element_by_css_selector('.header:nth-child(2)').click()   #通过class定位可以省略前面的标签
# driver.find_element_by_css_selector('#cart_num').click() #通过id来进行定位
# driver.find_element_by_css_selector("i[id='cart_num']").click()  #通过标准的属性进行定位
# driver.find_element_by_css_selector("div[class='logo_bar']>div :nth-child(2)>div:nth-child(2)>a:nth-child(4)").click()


from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://support.qq.com/products/14800')
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_css_selector("html>body>div>div>div>div>div>div>div[class='label_list__item']").click()
