# import sys
# print(sys.getdefaultencoding())        #查看编码方式
#
# print(3+2,5-1,2*3,5/2)         # 加减乘除
# print(5%2)                   # 取余
# print(5//2)                #向下取整
# print(5//-2)
#
# print(3**2)
# print(3**5)
#
# print('test'=='Test')           # 字符串之间比大小
# print(not 6.3>6.5)      # 逻辑结构and or not
# print(2>3 or 3>2)
# print(2>3 and 3>1)
# print('123'>'4')          # 容易混淆
# print(123>4)

# print(123>'4')  #字符串和数字不能比较
# print(r'仙子\n真漂亮')    #加上r当做字符串
# print('仙子\n真漂亮')
# l_1 = []                      #列表
# print(type(l_1))
# t_1 = ()
# print(type(t_1))
# t_1 = (12)                    #单个数据的时候，元组显示元组的类型
# print(type(t_1))
# l_1 = [1,'adshj',1.5,(1,1.5)]
# print(type(l_1))
# t_1 = (1,2)
# print(type(t_1))
# t_1 = (1,2,'四川菜')
# print(type(t_1))
# p_1 = ((15))
# print(p_1)
# p_1 = ((15,))
# print(p_1)
# l = ['adcd',13,12.5,True,(12,12.9,False)]
# print(l)
# l.append('大海的')  #添加
# l.append(13)
# l.append(15)
# print(l)
# l[0] = 999                 #修改
# print(l)
# l.remove(12.5)              # 删除
# print(l.count(13))         #count 统计出现的个数，只统计里面的个数，不统计里面的里面的
# n = (1,12,12.5,'ssfs',(1,12.5),['adcd',13,12.5,True,(12,12.9,False)])  # 元组里面的数据不能够修改，但是元组里面的数据可以进行修改的时候，可以进行修改
# print(n)
# n[5][0]=999
# n[5][1]
# print(n)       #元组里面的可修改的元素的内容修改
# m = [10,9,4,6,4,2,8,1,4,3,9]
# print(m)
# print(sorted(m)) #排序升序
# print(m)  #列表本身没改
# m.sort(reverse=True) #reverse为反转 sort为该变内容的排序
# print(m)
# m = ['assddfgdfh','asc','bdfcd','asdf','asdfg']
# print(sorted(m,reverse=True))
# m.sort(reverse=True,key=len)#长度降序
# print(m)

# m = ('assddfgdfh','asc','bdfcd','asdf','asdfg') #元组不能够用sort
# print(sorted(m,reverse=True))

# a = {'ip':'127.0.0.1'}  #创建字典
# a['ip']     #取字典中的元素
# print(a['ip'])
# a['port']=80   #插入新的键值对
# print(a)  #多个键值对 用逗号相隔

# dict_1 ={12:8080}
# print(dict_1)
# dict_1['ip1']='172.90.90.78'
# dict_1['ip1']='173.90.90.78'#key值相同，键值进行修改
# dict_1['ip2']='180.90.90.90'
# # print(dict_1)
# # # dict_1.clear()    #全部清空
# del dict_1['ip2']   # 删除其中一个
# # print(dict_1)
# # myip =dict_1.pop('ip1')     #删除其中一个，并保留了值
# # print(myip)
# print(dict_1['ip1'])
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items)
# a = 2
# b =3
# c = a
# a = b
# b = c
# print(a)
# print(b)
# a,b = 4,5
# a,b = b,a
# print(a)
# print(b)


# 作业

# a = input('请输入自己的英文名字=')
# dict_1={}
# dict_1['name'] = a
# # b = a[::-1]
# b = dict_1['name'][::-1]
# dict_1['new_name'] = b
# real_name=dict_1['name']
# print('您的英文名字是：%s' %real_name,'你的英文名字翻转为：',dict_1['new_name'])
# b = dict_1['name']
# b = b[::-1]
# b = sorted(dict_1['name'],reverse=True)
# dict_1['new_name'] = b
# print(b)



# 作业2
# grade = (input('请按照顺序输入各科的成绩'))
# grade = grade.split(',')
# print(grade)
# print(len(grade))
# for n in range(len(grade)):
#     grade[n] = int(grade[n])
#     print(grade)
# print((sorted(grade))[-1])
# math = float(input('请输入数学成绩：'))
# Chinese = float(input('请输入数学成绩：'))
# english = float(input('请输入数学成绩:'))
# general = float(input('请输入数学成绩:'))
# list = [math,Chinese,english,general]
# list.sort(reverse=True)
# # print(list)
# print('您的最高的一门成绩是：',list[0])



# 作业 3
# a = int(input('请输入第一个数字:'))
# b = int(input('请输入第一个数字:'))
# a = a+b
# print('两数之和为=%d'  %a)

# import test03
# test03.diancan(可乐鸡翅=1)
# print(__name__)
# from test03 import diancan
# diancan(可乐鸡翅=1)

# print(sum((12,34,56,78)))
# def odds(*p):
#      print(type(p))
#      print(sum(p))
# odds(1,2,3)


# a = int(input('请输入论坛积分'))
# if a<10000:
#     print('初入江湖')
# elif a<30000:
#    print('小有名气')
# else:
#    print('测试大牛')
import random

a = int(input('请输入整数N'))
b = []
for i in range(a):
    c = random.randint(1,10)
    b.append(c)
print(b)
for i in range(len(b)):
    for j in range(len(b)-1):
        if b[j]>b[j+1]:
            b[j],b[j+1]=b[j+1],b[j]
print(b)
c=[]
for i in range(len(b)-1):
    c.append(abs(b[i]-b[i+1]))
print(sorted(c)[0])
# a = 'bcbx bcbx bcbx'
# b =a.count('bcbx')
# print(b)
# a = open('test10.csv','r')
# b = ''
# for n in a:
#     b= b+n
# print(b)
# b = b.count('bcbx')
# print(b)