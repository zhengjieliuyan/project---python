from appium import  webdriver
import unittest
import time
import os
class Androidtest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 对字典赋值
        desired_caps['platformVersion'] = '5.1'  # 手机版本
        desired_caps['deviceName'] = 'Android Emulator'  # 默认的安卓模拟器
        # desired_caps['noResct'] = 'True'  #不清除之前的数据
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'  # 包名唯一的
        desired_caps['appActivity'] = '.ui.base.SplashActivity'  # 一个界面对应一个Activity，存在公用，拉起首个界面--启动的界面,web 一个URL对应的一个界面
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(40)
    def tearDown(self):
        # self.driver.quit()
        pass

# xpath通过id查找单个元素
    def test_01(self):
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass
            # self.driver.find_element_by_class_name('android.widget.TextView').click()  #默认第一个
        self.driver.find_element_by_xpath("//*[@resource id='cn.xiaochuankeji.tieba:id/title']").click()  #定位单个元素
        el = self.driver.find_elements_by_xpath("//*[@resource id='cn.xiaochuankeji.tieba:id/title']")   #定位多个元素，输出为列表
        el[3].click()
# xpath通过文本来进行定位
    def test_02(self):
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass
            # self.driver.find_element_by_class_name('android.widget.TextView').click()  #默认第一个
        el01 = self.driver.find_element_by_xpath("//*[@text='图文']")
        el01.click()
        self.driver.implicitly_wait(15)
        el02 = self.driver.find_elements_by_xpath("//*[@class='android.widget.ImageView']")
        el02[2].click()
# xpath通过class查找单个元素来定位
# xpath通过组合元素定位
# xpath通过父找子来定位
# xpath通过子找父来定位
#xpath 和web端一样的