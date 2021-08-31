from appium import  webdriver
import unittest
import time
import os
from appium.webdriver.common.touch_action import TouchAction
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
#点击click（）、sendkeys（）、获取文本信息（图片获得不了）
#keycode  按键操作
    def test_01(self):
        self.driver.keyevent(86)   #直接传对应的键值，直接在百度上搜索keycode
#截图操作
    def test_02(self):
        self.driver.get_screenshot_as_file('图片路径+图片地址')





