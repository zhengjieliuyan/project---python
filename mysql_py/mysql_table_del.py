#
#语句向表
#user_info_table
#插入记录
import time

import pymysql

#打开数据库连接
db = pymysql.connect(host="175.24.117.226", user="root", password="DpKuM$pNu6r%kcId",port=3307,database="liuyan")#可以指定一个数据库--可以减少使用命令use 数据库名字
#使用cursor()方法创建一个游标对象--窗体 cursor
result = db.cursor()

#使用excute()方法执行sql查询
# result.execute("drop table if EXISTS 数据表名字")  #执行完还是在result上  工作不建议用
# result.execute("show tables")
# data = result.fetchall()      #执行的数据拿出来
# print(data)

#建数据表
# sql = '''create table  if not EXISTS zhengjie(user_id int(11) NOT NULL AUTO_INCREMENT,
# user_name char(10),
# password varchar(10),
# user_nick varchar(30),
# card_num bigint(20),
# PRIMARY KEY(user_id))'''
#
# result.execute(sql) #建数据库也看不出什么来,删除也看不出来
# result.execute('show tables')
# data = result.fetchall()      #执行的数据拿出来
# print(data)


#在数据表中插入数据
# mysql_py = '''insert into zhengjie (user_id,user_name,password,user_nick,card_num) values ('120','asddsa','sada','fsaas','12324324')'''
#
# result.execute(mysql_py)
# print('insert into mysql_py is ok')
# time.sleep(10)
# db.commit()        #等待提交
# mysql_py = '''insert into zhengjie (user_id,user_name,password,user_nick,card_num) values ('111','asddsa','sada','fsaas','12324324')'''
# try:
#     for n in range(100):
#          mysql_new = mysql_py.replace('111',str(n+100))
#          print(n)
#          # print(mysql_new)
#          result.execute(mysql_new)
#     print('insert into mysql_py is ok')
#     db.commit()         #只有循环完成才可以提交
# except:
#     db.rollback()       #清除之前没有完成的数据未提交，
#     print('error')


#del删除数据
# dl = "delete from zhengjie where user_id = '130'"   #赋值变量于命令
# result.execute(dl)
# db.commit()#执行命令  不要忘记提交
# data = result.fetchall()      #执行的数据拿出来
# print(data)
try:
    for n in range(100,200):
        dl = ("delete from zhengjie where user_id = %d" %n)
        result.execute(dl)
        db.commit()

except:
    db.rollback()
    print('error')









#关闭数据库
db.close()
