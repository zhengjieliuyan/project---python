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
#获取手机的分辨率
    def test_01(self):
        height =self.driver.get_window_size()['height']  #返回类型为字典
        width = self.driver.get_window_size()['width']
    def test_02(self):
        self.driver.implicitly_wait(60)

        el = self.driver.find_element_by_id("")
        cur_activity = self.driver.current_activity  #获取当前界面  web端通过URL  基本不会用到
        print(cur_activity)
        print(el.get_attribute("className"))  #获取当前控件的属性值
        print(el.get_attribute("resourceId"))
        print(el.is_displayed())  #判断控件是否显示  ---页面有办法可以让控件不显示
        print(el.is_enabled())   #判断控件是否可用

    def test_03(self):
        self.driver.implicitly_wait(45)


        self.driver.swipe(500,100,500,200,3000)#初始的x,y坐标，结束的x,y坐标，以及实现这个动作的时间毫秒----页面滑动
        self.driver.swipe(500,200,500,200,100)#表示常按，左上角为（0,0），右下角为最大
        self.driver.swipe(500, 200, 500, 200, 100)#这个方法不好用，针对不同的手机
        #上划、下划、左划、右划
    def test_05(self):
        height = self.driver.get_window_size()['height']  # 返回类型为字典
        width = self.driver.get_window_size()['width']
        self.driver.swipe(width*0.7,height*0.86,width*0.7,height*0.13,3000)  #最好使用这个                         #定位控件的百分比
    def test_06(self):
        self.driver.implicitly_wait(40)
        try:
            self.driver.find_element_by_xpath("//*[@text='我知道了']").click()
        except:
            pass
        el = self.driver.find_elements_by_xpath("//*[@class='android.widget.TextView']")
        j=1
        for i in el:
            i = i.text
            print('第'+str(j)+'个'+i)
            j=j+1
        #控件点击
        # TouchAction(self.driver).tap(el).perform()  #tap 点击 perform把之前的动作执行
        # #坐标点击
        # TouchAction(self.driver).tap(x=100,y=140).perform()
        # #press 某个点
        # TouchAction(self.driver).press(x=100,y=140).release().perform()
        # #长按某个点
        # TouchAction(self.driver).long_press(x=100,y=140,duration=5000).release().perform()
        # #控件长按
        el =self.driver.find_elements_by_xpath("//*[@class='android.widget.TextView']")
        TouchAction(self.driver).long_press(el[5]).release().perform()  #定位控件




















