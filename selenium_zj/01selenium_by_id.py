# from selenium import webdriver     #引用
#
# driver = webdriver.Chrome()
# driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# driver.maximize_window()    #最大化web页面
#
# driver.find_element_by_id('nav_more').click()

from selenium import webdriver     #引用

driver=webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')
driver.maximize_window()    #最大化web页面

driver.find_element_by_id('cart_num').click()