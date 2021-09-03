# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains   #导入模块下的一个类
# d = webdriver.Chrome()
# d.get('https://passport.bilibili.com/login?from_spm_id=333.999.top_bar.login_window')
# time.sleep(3)
# d.maximize_window()
# e = d.find_element_by_xpath("//a[text()='美食特产']")

# ActionChains(d).move_to_element(e).perform()    #d 为必须传输的实参   e为定位的控件  perform 运行储存的动作
# time.sleep(3)                                    #move to为移动的
# ActionChains(d).context_click(e).perform()    #context_click 右击
# time.sleep(3)
# ActionChains(d).double_click(e).perform()    #左击两次

# d.find_element_by_xpath("//*[@type='text'and@placeholder='你的手机号/邮箱']").send_keys('18319731403')
# d.find_element_by_xpath("//*[@type='password'and@placeholder='密码']").send_keys('zj090126')
# d.find_element_by_xpath("//*[@class='btn btn-login']").click()
# time.sleep(3)
# f = d.find_element_by_css_selector("div[class='geetest_slider_button']")
# time.sleep(5)
#
# ActionChains(d).drag_and_drop_by_offset(f,400,0)

from selenium.webdriver.common.keys import Keys#先导入keys这个类
from selenium import webdriver

# import time
# driver=webdriver.Chrome()
# driver.get('http://101.133.169.100/yuns/index.php')
#
# driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys("女装")
# driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]")#模拟输入女装后回车Keys.按键
# time.sleep(2)



#滑块验证
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains   #导入模块下的一个类
d = webdriver.Chrome()
d.get('http://101.133.169.100:8088/index.html#/login')
time.sleep(3)
d.maximize_window()
time.sleep(8)
'''
d.execute_script('window.scrollTo(0,300)')   #滚动部分
time.sleep(3)
f = d.find_element_by_xpath("//*[@class='yidun_slider']")
time.sleep(3)
e = d.find_element_by_xpath("//*[@class='yidun_tips']").size
e = e['width']*0.5
#
ActionChains(d).drag_and_drop_by_offset(f,e,0)    #滑块的拖拽
'''
# ActionChains(d).drag_and_drop(f,target)        #滑块移动到具体的控件
d.find_element_by_xpath("//*[@name='username']").send_keys('18319731410')
d.find_element_by_xpath("//*[@name='password']").send_keys('123456')
d.find_element_by_xpath("//*[@class='el-button submit-btn el-button--default']").click()
time.sleep(5)
d.find_element_by_xpath("//*[@class='el-icon-caret-bottom mark']").click()
time.sleep(5)
d.find_element_by_xpath("//*[@class='el-button handel-button el-button--primary']/span").click()
time.sleep(3)
d.find_element_by_xpath("//*[@href='#/manager/system-project']/../li[2]/div").click()
time.sleep(3)
d.find_element_by_xpath("//a[@href='#/manager/custom-field']/li").click()
time.sleep(5)
d.find_element_by_xpath("//*[@class='table-box']/div[1]/div[3]/button[1]/span").click()
time.sleep(3)
f = d.find_element_by_xpath("//*[@class='list-wrapper']/li[1]")
ActionChains(d).drag_and_drop_by_offset(f,350,0).perform()  # perfrom 执行存储的动作

g = d.find_element_by_xpath("//*[@class='field-info-section']/div[1]")
h = d.find_element_by_xpath("//*[@class='list-wrapper']/li[2]")
ActionChains(d).drag_and_drop(h,g).perform()          #perform 记住执行




