from selenium import webdriver
import time
drive = webdriver.Chrome()
drive.get('http://101.133.169.100/yuns/index.php/')
time.sleep(3)
drive.maximize_window()
# drive.find_element_by_tag_name('div').click()
a = drive.find_elements_by_tag_name('div')
print(len(a))
print(a)
