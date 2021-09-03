#
#语句向表
#user_info_table
#插入记录
import time

import pymysql

#打开数据库连接
db = pymysql.connect(host="175.24.117.226", user="root", password="DpKuM$pNu6r%kcId",port=3307,database="liuyan")#可以指定一个数据库
#使用cursor()方法创建一个游标对象--窗体 cursor
result = db.cursor()

#使用excute()方法执行sql查询
# result.execute("drop table if EXISTS 数据表名字")  #执行完还是在result上  工作不建议用
result.execute("show tables")
data = result.fetchall()      #执行的数据拿出来
print(data)

#建数据表
sql = '''create table  if not EXISTS zhengjie(user_id int(11) NOT NULL AUTO_INCREMENT,
user_name char(10),
password varchar(10),
user_nick varchar(30),
card_num bigint(20),
PRIMARY KEY(user_id))'''

result.execute(sql) #建数据库也看不出什么来,删除也看不出来
result.execute('show tables')
data = result.fetchall()      #执行的数据拿出来
print(data)

#sql 插入语句
mysql ='''insert into zhengjie(user_id,user_name,password,user_nick,card_num)values
('120','sgag','ffj','sfhaj','124253')'''
result.execute(mysql)
print("mysql插入成功")
time.sleep(10)
db.commit()   #提交
mysql ='''insert into zhengjie (user_id,user_name,password,user_nick,card_num) values ('111','asddsa','sada','fsaas','12324324')'''
try:          #try和expect要搭配使用
#执行sql语句
    for n in range(100):
        mysql_q = mysql.replace('111',str(n+100))
        result.execute(mysql_q)
    time.sleep(10)
    db.commit()
except:
    db.rollback()
    print("error")

#关闭数据库
db.close()
