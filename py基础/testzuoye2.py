#1.使用Python输出99乘法表
# for i in range(1,10):
#     for n in range(1,i+1):
#         print('%s*%s=%s' %(i,n,i*n),end='   ')
#     print('')

# 2.用python实现冒泡算法，给你一个包含若干值的列表，将他们从小到大排序输出（不能用sort或者sorted,自己用代码实现）
#冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序（如从大到小、首字母从Z到A）错误就把他们交换过来
# eg:
# maopao([2,1,8,4,3,6])
# 输出结果：[1,2,3,4,6,8]
# maopao = [7,89,34,3,2,7,90,76]
# # print(maopao[1])
# for m in range(len(maopao)):
#     for n in range(len(maopao)-1):
#         if maopao[n]>maopao[n+1]:
#             maopao[n],maopao[n+1]=maopao[n+1],maopao[n]
# print(maopao)
# 3.猜数字游戏
# 代码中生成一个随机整数. 然后用户输入数字后, 程序提示用户的输入是高了还是低了. 直到用户猜中这个数字,
#游戏结束. 提示, random模块的randint函数能够帮助我们生成随机整数. (import random )
# import random
# a = random.randint(1,10)
# print(a)
# b = int(input('请输入数字：'))
# while a !=b:
#     if a>b:
#         print('用户输入低了')
#         b = int(input('请输入数字：'))
#     elif a<b:
#         print('用户输入高了')
#         b = int(input('请输入数字：'))
# print('游戏结束，输入正确')

# 4.打开一个txt文本，找一首诗写入此文本，
#2)读取一个不存在的文件，处理异常，不能让程序停下来，而是能够继续读取存在文件里的文本内容，并输出这首诗
# write = open('test03.csv','a',encoding='utf-8')
# write.write('\n窗前明月光,\n疑是地上霜,\n举头望明月,\n低头思故乡')
# try:
#     read = open('test05.csv','r')
# except Exception as error:
#     print('错在第40行')
#     print(error,'type(eror)')
#     raed = open('test03.csv', 'r',encoding='utf-8')
#     for n in raed:
#         n = n.strip()
#         print(n)
# 5.创建一个包，包下面创建一个模块,模块里定义一个长方形类，实例化时需要传入参数：长、宽（使用__init__方法）
# 拥有两个方法：
# 1)求周长
# 2)求面积
# 再创建一个模块，导入上一个类，实例化这个类，调用他的两个方法
#
#
#
# 6.把今天讲的内容自己全部练习一遍,整理笔记到 wiki目录
# import zuoye5
# zuoye5.lei(3,5)