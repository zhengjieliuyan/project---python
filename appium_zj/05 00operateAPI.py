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
#点击click（）、sendkeys（）、获取文本信息（图片获得不了）
#获取手机的分辨率
    def test_01(self):
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass
        height =self.driver.get_window_size()['height']  #返回类型为字典
        width = self.driver.get_window_size()['width']
        print(height,width)
    def test_02(self):
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/ic_search_b']").click()
        self.driver.find_element_by_xpath("//*[@text='搜索话题 / 帖子 / 用户']").send_keys('sdafafg')
        # self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/iconTabItem']").click()

