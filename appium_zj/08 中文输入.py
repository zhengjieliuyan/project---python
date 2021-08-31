from appium import  webdriver
import unittest
import time
import os
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
class Androidtest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 对字典赋值
        desired_caps['platformVersion'] = '5.1'  # 手机版本
        desired_caps['deviceName'] = 'Android Emulator'  # 默认的安卓模拟器
        # desired_caps['noReset'] = 'True'  #不清除之前的数据
        desired_caps['fullReset']='True'   #重置APP 每一次跑完会把APP卸载掉
        desired_caps['app']='d:/zuiyou518.apk'  #给一个apk路径，安装这个app 确保每一次用例独立，但是速度很慢
        desired_caps['unicodeKeyboard'] = 'True'  # 添加一个中文输入法
        desired_caps['resetKeyboard'] = 'True'  # 键盘重置
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'  # 包名唯一的
        desired_caps['appActivity'] = '.ui.base.SplashActivity'  # 一个界面对应一个Activity，存在公用，拉起首个界面--启动的界面,web 一个URL对应的一个界面
        desired_caps['automationName']='Uiautomator2'   #抓获toast时使用---添加参数

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        # self.driver.quit()
        pass
    def test_01(self):
        #黑框消失很快，比如‘评论成功’
        self.driver.implicitly_wait(100)
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass
        self.driver.find_elements_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/textTabItem']")[3].click()
        self.driver.find_element_by_xpath("//*[@text='立即登录/注册']").click()
        self.driver.find_element_by_xpath("//*[@text='密码登录']").click()
        self.driver.find_element_by_xpath("//*[@text='请输入手机号']").send_keys('15127409611')
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/code_edit']").send_keys('a123456')
        self.driver.find_element_by_xpath("//*[@text='登  录']").click()
        self.driver.keyevent(4)
        self.driver.find_elements_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/textTabItem']")[0].click()
        self.driver.find_elements_by_xpath("//*[@class='android.widget.TextView']")[5].click()
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/etInput']").send_keys('太丑了，卧槽')
        self.driver.find_element_by_xpath("//*[@text='发送']").click()

        


        toast = ("xpath","//*[contains(@text,'评论发送成功')]")   #元组
        el = WebDriverWait(self.driver,20,0.1).until(EC.presence_of_element_located(toast))
        print(el.text)    #最大等待时间20s 每隔0.1秒进行检查







