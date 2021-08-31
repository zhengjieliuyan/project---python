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

    def tearDown(self):
        # self.driver.quit()
        pass
    def test_01(self):
        self.driver.find_element_by_class_name('android.widget.TextView').click()  #默认第一个

    def test_02(self):
        self.driver.find_elements_by_class_name("android.widget.TextView")[3].click()      #查找到的为id这样的全部，然后为list类型
        el = self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in range(0,len(el)):            #for 循环找具体的属性值的文本信息，或者在页面上一个一个找
            print('第'+i+'个'+el[i].text)



