#
#语句向表
#user_info_table
#插入记录
import pymysql

#打开数据库连接
db = pymysql.connect(host="175.24.117.226", user="root", password="DpKuM$pNu6r%kcId",port=3307)
#使用cursor()方法创建一个游标对象--窗体 cursor
result = db.cursor()

#使用excute()方法执行sql查询
result.execute("drop database if EXISTS 数据库名字")  #执行完还是在result上  工作不建议用
data = result.fetchall()      #执行的数据拿出来
print(data)
result.execute('show databases')
data = result.fetchall()    #使用fetchone（）方法获取单条数据
print(data)
#建数据库
result.execute("create database  if not EXISTS liuyan character set 'utf8'")  #建数据库也看不出什么来,删除也看不出来

#使用excute()方法执行sql查询
result.execute('show databases')
#使用fetchall方法获取所有结果
# data = result.fetchall()
# data_2 = result.fetchone()    #返回值为NONE
data_2 = result.fetchone()   #有点类似读写
data = result.fetchall()
print(data_2)        #拿的元组里面下标为0 的元素
print(data)      #打印值为元组
#关闭数据库
db.close()
