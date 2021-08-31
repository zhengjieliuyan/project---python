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
        height =self.driver.get_window_size()['height']  #返回类型为字典
        width = self.driver.get_window_size()['width']
    def test_02(self):
        self.driver.implicitly_wait(60)
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass

        el = self.driver.find_element_by_id("")
        cur_activity = self.driver.current_activity  #获取当前界面  web端通过URL  基本不会用到
        print(cur_activity)
        print(el.get_attribute("className"))  #获取当前控件的属性值
        print(el.get_attribute("resourceId"))
        print(el.is_displayed())  #判断控件是否显示  ---页面有办法可以让控件不显示
        print(el.is_enabled())   #判断控件是否可用

    def test_03(self):
        self.driver.implicitly_wait(45)
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass

        # self.driver.swipe(500,1000,500,100,3000)#初始的x,y坐标，结束的x,y坐标，以及实现这个动作的时间毫秒----页面滑动
        # self.driver.swipe(500,200,500,200,100)#表示常按，左上角为（0,0），右下角为最大
        self.driver.swipe(500, 200, 500, 200, 5000)#这个方法不好用，针对不同的手机
    def test_05(self):
        self.driver.implicitly_wait(50)
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()  # 对于弹出来的控件处理
        except:
            pass
        height = self.driver.get_window_size()['height']  # 返回类型为字典
        width = self.driver.get_window_size()['width']
        self.driver.swipe(width*0.7,height*0.8,width*0.7,height*0,3000)  #最好使用这个                         #定位控件的百分比



