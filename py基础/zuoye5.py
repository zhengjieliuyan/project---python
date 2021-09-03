# 5.创建一个包，包下面创建一个模块,模块里定义一个长方形类，实例化时需要传入参数：长、宽（使用__init__方法）
# 拥有两个方法：
# 1)求周长
# 2)求面积
# 再创建一个模块，导入上一个类，实例化这个类，调用他的两个方法

# class lei():
#     def __init__(self,x,y):
#         self.x= x
#         self.y = y
#     def add(self):
#         s = self.x * self.y
#         print('长方形的面积：%s ' %s)
#     def odd(self):
#         l = 2 * (self.y + self.x)
#         print('长方形的周长%s' %l)
# xiaowen  = lei(3,5)
# xiaowen.odd()
# xiaowen.add()

# i = 1
# while i<10:
#     i = i + 1
#     for m in range(1,i):
#         print('%s*%s=%s' %(m,(i-1),(i-1)*m),end= '   ')
#     print('')
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print('%s*%s=%s' % (j, (i), (i) * j), end='   ')
#         j = j + 1
#     print('')
#     i= i+1

# m = input('请输入一组数据用,分隔：')
# m = m.split(',')
# print(m,type(m))
# for n in range(len(m)):
#     for k in range(len(m)-1):
#         m[k]=int(m[k])
#         if m[k]%2==0:
#             m[k],m[k+1]=m[k+1],m[k]
# print(m)

# bubble = input('请输入数字用,分隔:')
# bubble = bubble.split(',')
# print(bubble)
# for n in range(len(bubble)):
#     bubble[n]=int(bubble[n])
# print(bubble)
# i = 0
# while i<len(bubble):
#         for j in range(len(bubble)-1-i):
#             if bubble[j] > bubble[j+1]:
#                 bubble[j],bubble[j+1] = bubble[j+1],bubble[j]
#         i = i+1
# print(bubble)
def bubble(demo):
    num = len(demo)
    for m in range(num):
         for j in range(num-1-m):
            if demo[j] > demo[j+1]:
                    demo[j],demo[j+1] = demo[j+1],demo[j]
    print(demo)
bubble([12,45,78,32,15,34])
print([12,45,67][1])