from appium import  webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'  #对字典赋值
desired_caps['platformVersion'] = '5.1'     #手机版本
desired_caps['deviceName']='Android Emulator'           #默认的安卓模拟器
desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'         #包名唯一的
desired_caps['appActivity'] = '.ui.base.SplashActivity'        #一个界面对应一个Activity，存在公用，拉起首个界面--启动的界面,web 一个URL对应的一个界面
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(50)
# driver.find_elements_by_id('cn.xiaochuankeji.tieba:id/iconTabItcm')[1].click()    #错误的


# from appium import webdriver
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1'
# desired_caps['deviceName'] = 'Android Emulator'
# # desired_caps['noReset'] = 'True'
# # desired_caps['app'] = PATH('D:/zuiyou518.apk')
# # desired_caps['unicodeKeyboard'] = 'True'
# # desired_caps['resetKeyboard'] = 'True'
# desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
# desired_caps['appActivity'] = '.ui.base.SplashActivity'
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.implicitly_wait(50)
# driver.find_elements_by_id('cn.xiaochuankeji.tieba:id/iconTabItcm')[1].click()
