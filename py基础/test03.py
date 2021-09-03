# word = 'hello python zhengjie'
# print(word.replace('python','liuyan'))
# word = 'hello python python  zhengjie'
# print(word.replace('python','liuyan'))
# print(str(4))
# sql_demo = "insert into table values (1,'bcbx')"
# print(sql_demo)
# b = sql_demo.replace('bcbx','zhengjie')
# for n in range(1,10,2):    #:容易忘记
#     print(sql_demo.replace('bcbx',str(n)))

# word = 'abcd'
# print(word.isalpha())     #变量名.isalpha()判断是否为纯字符串
# word = 'abcd8'
# print(word.isalpha())
# print(word.isdigit())  #变量名.isalpha()判断是否为纯字符串
# word = '123458'
# print(word.isdigit())
# word = '1.23458'      #小数点不是纯数字
# print(word.isdigit())
# word_3 = 'hello every day is rainning'
# print(word_3.find('iso'))  #找不到返回-1
# word_3 = 'hello every day is rainning'
# print(word_3.find('y'))  #多个找第一个
# word_3 = 'hello every day is rainning'
# print(word_3.find('day'))  #找到第一个定位数字


# word_3 = 'hello every day is rainning'
# print(word_3.startswith('hell'))  #判断开头或结尾
# print(word_3.endswith('ing'))

# word_3 = '    hello every day is rainning' #去除字符串的前后空格/及换行符
# print(word_3)
# print(word_3.strip())
# word_3 = '    hello every day is rainning    \n'
# print(word_3)
# b = '_'
# a = ['aa','bb','cc','dd']
# print(b.join(a))    #将序列中的字符串合并成一个字符串
# b = 'ee'
# print(b.join(a))
#
# a = 'zheng jie'
# print(a.split())   #默认按照空格来切割
# a = 'zh,eng, ji,e'
# print(a.split(','))
# score_list = input('请输入各科成绩，逗号分隔')
# print(score_list)
# print(score_list.split(','))  #分隔后变成列表list

# a =['abc',1234]              #列表比较
# b = ['cdb',789]
# print(a>b)
# print(id(88),type(88),88)         # 对象三要素，id,type,value
# 标准的if条件语句语法为如下
# 如果表达式的值为非0或者布尔值True，则执行do_something,否则执行下一句语句
#'' {} [] () 空值不能做if的语句
# if 3>2:       #注意加：
#     print('i am 1')
# print('i am 2')

# if 3<2:       #注意加：
#     print('i am 1')
# else:
#     print('i am 3')
# print('i am 2')

# score_math = int(input('你的数学成绩'))
# if score_math>100 or score_math<0:
#     score_math = int(input('请输入0-100的成绩'))
# elif score_math>80:
#     print('评级优秀')
# elif score_math>75:
#     print('评级良好')
# elif score_math>60:
#     print('评级及格')
# else:
#     print('评级不及格')

# x,y = 5,3
# if x>0:
#     if y>0:          # if的嵌套使用
#         print('x and y >0')
# else:
#     print('x or y < 0')

x,y,smaller = 9,4,0
# if x>y:
#     smaller = x
#     print(smaller)
# else:
#     smaller = y
#     print(smaller)
# smaller = x if x>y else y  #装逼写法不推荐。
# print(smaller)

#while循环语句和if语句语法类似，只要表达式的值非0 或者为True，就会循环执行。
# while 3 >2:    #死循环
#     print('zhengjie')
# n = 1
# while 3 >n:
#     print('zhengjie')
#     n+=1
# n = 1
# score_math = int(input('你的数学成绩'))
# while n<=3:
#     if score_math>80:
#      print('评级优秀')
#     else:
#     break
# if score_math>75:
#      print('评级良好')
# elif score_math>60:
#     print('评级及格')
# else:
#     print('评级不及格')

#for循环
#Python中的for循环和传统的for循环不太一样
#for循环接收可迭代对象（序列或者迭代器）作为参数，每次迭代其中的一个元素
# Word ='welcome to zhengjie'
# for n in Word:
#     print(n)
# list_1 = [1,'10','asdkjsfg','gfasg']
# for n in list_1:
#     print(n)
# list_1 = (1,'10','asdkjsfg','gfasg')
# for n in list_1:
#     print(n)
# dict_1 = {'ip':'172.78.90.0','port':'8080'}
# for n in dict_1:     #字典返回的为key值
#     print(n)
# dict_1 = {'ip':'172.78.90.0','port':'8080'}
# for n in dict_1.keys():     #字典的三个特殊keys、values、items
#     print(n)
# dict_1 = {'ip':'172.78.90.0','port':'8080'}
# for n in dict_1.values():     #字典的三个特殊keys、values、items
#     print(n)
# dict_1 = {'ip':'172.78.90.0','port':'8080'}
# for n,m in dict_1.items():     #字典的三个特殊keys、values、items
#     print(n)
#     print(m)
#内建函数range
#内建函数range能够生成一个数字组成的列表，方便进行for循环
# list_1 = [1,2,Ture,'zhengjie']
# print(len(list_1))
# for n in range(1,10,2):  #range(1,10,2) 1为开始值，10 为循环的总个数。2为步长
# for n in range(len(list_1)): #for和list经常搭配使用
# grade = (input('请按照顺序输入各科的成绩'))
# grade = grade.split(',')
# print(grade)
# print(len(grade))  #获取列表内容元素的个数
# for n in range(len(grade)):
#     grade[n] = int(grade[n])#通过下标来进行修改
#     print(grade)
# print(sorted(grade)[-1])

#abs:求一个数的绝对值
#divimod:返回一个元组，同时计算商和余数
# a = 10
# print(abs(a))
# a,b = divmod(10,3)
# print(a,b)
#round:对浮点数进行四舍五入
#round有两个参数，第一个是要进行运算的值，第二个是保留小数点后多少
# print(round(3.54789,3))
# print(round(3.54789,2))
# #程序在处理浮点型小数时，会有精度误差
# print(round(3.525,2))

#break、continue和pass
#使用break语句跳出当前循环
#查找[1,100)第一个3的倍数
# for n in range(1,100):
#     if n%3 ==0:
#         print(n)
#         break  #终止循环


# for n in range(1,100):
#     if n%3 !=0:
#         pass   #表示通过  表示占位符
#     else:
#         print(n)
#使用continue语句，回到循环顶端，判定循环条件；
#循环条件满足，则执行下一次循环；
# for n in range(1,100):
#     if n%3 !=0:
#         continue   #表示继续  表示跳过
#     print(n)
#生成[0,4)的数字的平方列表
# list_1 = []
# for n in range(4):
#     list_1.append(n**2)
#     print(list_1)
#获取[0,,8)区间中所有的奇数
# list_odd = []
# for n in range(1,8):
#     if n%2 !=0:
#         print(n)
#         list_odd.append(n)
# print(list_odd)
#
# list_odd = [n for n in range(8) if n%2 ==0]    #装逼写法，不建议
# print(list_odd)
#函数
#一些可以重复使用的代码，可以提取出来放到函数中，
#Python使用def来定义一个函数，使用return来返回结果
# def add(x,y):
#     return x+y
# #调用函数
# print(add(1,2))
#理解‘形参’和‘实参’：形参相当于数学中‘未知数’这样的概念，实参就是
#Python中相同名字的函数，后面的会覆盖前面的。

# def diancan1(food='可乐鸡翅',num=1): #可以给默认值，默认值的放在后面
#     dict = {'蛋炒饭':15,'可乐鸡翅':40,'面包':5}
#     total_fee = dict[food]*num
#     print('你点的餐需要支付%d' %total_fee)
#     return    total_fee ,dict       #函数里面的变量外面用不了，除非return
# # ly,z_j = diancan('可乐鸡翅',2)  #返回的变量
# # print(z_j['面包'])
# diancan('蛋炒饭',10)

# def diancan(num=1,*foods): #使用*不能够给变量值，因为输出的为元组，元组不可变
#     dict = {'蛋炒饭':15,'可乐鸡翅':40,'面包':5}
#     print(foods,type(foods))
#     total_fee = 0
#     for food in foods:
#         print(food)
#         total_fee =  total_fee+dict[food]*num
#         print(total_fee)
#     print('你点的餐需要支付%d' %total_fee)
#     return    total_fee ,dict
# diancan(1,'可乐鸡翅','蛋炒饭','面包')#对应上传多个菜品使用*





# def diancan(**num): #**处理数据为字典
#      dict = {'蛋炒饭':15,'可乐鸡翅':40,'面包':5}
#      print(__name__,type(__name__))
#      print(num,type(num))
#      total_fee = 0
#      for food in num:
#         print(food)
#         total_fee =  total_fee+dict[food]*num[food]
#         print(total_fee)
#         print('你点的餐需要支付%d' %total_fee)
#         return    total_fee ,dict
# diancan(可乐鸡翅=1,蛋炒饭=5,面包=5)#传的数量和菜品名字都不确定用**

#使用内建函数open打开一个文件；
#handle = open（file_name,'r'）
#file_name是文件的名字，可以是一个绝对路径也可以是相对路径。
#第二个位置是文件打开方式，选项有以下几种'r'只读'w'覆盖写'a'追加
#handle是一个文件句柄，是一个可迭代的对象，可以直接使用for循环按行读取文件
#handle使用完毕，需要close掉，否则会引起资源泄露（一个进程能打开的句柄数目）
#handle.close()
# read_line = open('test-1.csv','r')
# print(read_line,type(read_line))
# for line in read_line:
#     line = line.strip()
#     print(line)
# print(read_line.read(10))
# print(read_line.readline())
# print(read_line.readline())
# print(read_line.readlines())   #读是接着上面读过的来读的，读到的内容为列表
# read_line.close()

write_line = open('px-01/test-2.csv', 'r', encoding='utf-8')
# write_line.write('student_01,123456')
# for m in range(1,10000):
#     write_line.write('student_%s,123456\n'%m)
#     print(write_line)
# write_line.close()
# for m in write_line:
#     m = m.split(',')
#     print(m)
# write_line.close()

# with open('test-2.csv','w',encoding='utf-8') as write_line:
#     for n in read_line:    #这种写法可以不用写close（）
#         n = n.strip()
#         n_list = n.split(',')
#         print(n_list[0])
#
#         break
#语法报错，直接报错，不报行数
#认识异常
# if __name__ == '__main__':
#     print('--------start---------------')
#     list_1 = [23,13,56,78]
#     try:
#         print(list_1[10])
#     except Exception as error:  #Exception错误的集合有点模糊，可以具体的
#         print(error)
#         print(type(error))
#         print('具体哪一行出错了')
#         print(list_1[-1])
#     print('--------end---------')
#我们使用try语句来捕捉异常（可能触发异常的代码放到try中），使用except来具体处理异常
#如果异常能够被except捕捉到，则不会影响程序继续进行。
#indexerror，e相当于捕捉到的这个异常对象的名字为e，这个异常对象包含了异常的具体信息
#目的不能让代码停下来。


#模块 Python 模块初始
#当代码量比较大的时候，我们最好把代码拆分成一些有组织的代码片段
#每个代码片段里面包含一组逻辑上有关联的函数或者类
#每一个片段里放在一个独立的文件中，这样的片段成为模块
#使用import可以在一个Python文件中引入其他的模块
#import记住，既然模块也是一个对象，那么也可以给这个对象赋值（相当于定义别名）
#实际上使用import-as可以更方便的完成这个动作；
#from-import语句
# import语句是直接导入一个模块。而有时我们只需要用到模块中的某一个或几个函数，就可以使用from-import
#一个py文件就是一个模块

#我们写import module时，其实有两个大的阶段。先将这个模块的文件加载到内存中，并创建一个来表示；然后通过一个变量名来将这个模块引入到当前的命名空间中。
#如果同一个模块（）被import了多次，其实加载动作只进行了一次
#if __name__ =='__main__'   #只能够在自己下面运行
#import test02 as t01   #对test02 进行重新命名
#from 模块 import 文件里面的函数
#from 模块 import 文件里面的函数 （*使用里面全部的函数）--这个可以直接使用里面的函数
#模块里面加前面加_的不能够被*导入
#创建一个包，里面默认有_init_.py模块，初始化操作的模块在这个里面写。
#定义了很多相同的函数，放在同一个下面为类。





#类
# class order():
#     def __init__(self,name):   #特殊的一种
#         self.name = name
#     def diancan(self,**num):  # **处理数据为字典  #在类中变量成为通用变量必须加self
#          if self.name =='柱间':
#              dict = {'蛋炒饭': 30, '可乐鸡翅': 90, '面包': 105}
#          elif self.name == '宇智波':
#              dict = {'蛋炒饭': 15, '可乐鸡翅': 40, '面包': 5}
#          print(__name__, type(__name__))
#          print(num, type(num))
#          total_fee = 0
#          for food in num:
#              print(food)
#              total_fee = total_fee + dict[food] * num[food]
#              print(total_fee)
#              self.all = total_fee
# #             print('你点的餐需要支付%d' % total_fee)
# #             return total_fee, dict
#     def finall(self,discount):
#         print('优惠后后的价钱为:',discount*self.all)
#
# # xiaowen = order('柱间')#实例化
# # xiaowen.diancan(可乐鸡翅=3)
# # xiaowen.finall(0.8)


# class son_of_zhengjie(order):             #类的继承关系
#     def welcome(self):
#         print('欢迎来到王者农药')
#
# xiaowen = son_of_zhengjie('宇智波')
# # xiaowen.diancan(可乐鸡翅=3)
# xiaowen.welcome()

