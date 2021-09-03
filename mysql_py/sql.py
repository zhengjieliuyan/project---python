# 数据库插入操作
# 以下实例使用执行
# SQL
# INSERT
# 语句向表
# user_info_table
# 插入记录：
import time
import pymysql

# 打开数据库连接
db =  pymysql.connect(host="175.24.117.226", user="root", password="DpKuM$pNu6r%kcId",port=3307)

# 使用cursor()方法获取操作游标   ---窗体
# cursor = db.cursor()




# SQL 插入语句
# sql = '''INSERT INTO `user_info_table` (`user_id`, `user_name`, `password`, `user_nick`, `card_num`) VALUES ('111', 'zhangsan', 'abc123', 'zhangsanfeng', '124567894651329785')'''
# cursor.execute(sql)
# print('insert sql ok')
# time.sleep(10)
# db.commit()
# try:
    # 执行sql语句
#     for  n in range(100):
#         sql_new = sql.replace('111',str(n+100))
#         print(n)
#         sql_new = sql_new.replace('zhangsan','zhangsan%d' %n)
#         # print(sql_new)
#         cursor.execute(sql_new)
#     print('insert sql ok')
#     # 提交到数据库执行
#     db.commit()
#     cursor.execute('select * from user_info_table')
#     rel = cursor.fetchall()
#     print(rel)
#
# except  Exception as e:
#     # 如果发生错误则回滚
#     db.rollback()
#     print(e,type(e))
#     sql = """INSERT INTO `user_info_table` (`user_id`, `user_name`, `password`, `user_nick`, `card_num`) VALUES ('224', 'zhangsan', 'abc123', 'zhangsanfeng', '124567894651329785')"""
#     cursor.execute(sql)
#     print('insert sql except ok')
#     time.sleep(5)
#     db.commit()
#     # db.rollback()
#     print('error')

# sql2='''INSERT INTO `user_info_table` (`user_id`, `user_name`, `password`, `user_nick`, `card_num`) VALUES
# ('3', 'wangwu', '123aaa', 'wangbaiwan',214567894651324567),
# ('4', 'liuqi', '12aaa', 'liuchuanfeng', 214563356651324567),
# ('5', 'zhangliu', '12aaa', 'zhangwuji', 214563356658966567)'''
#
# cursor.execute(sql2)
# db.commit()
# 关闭数据库连接
# db.close()



# 以下代码使用变量向SQL语句中传递参数:
# ..................................
# user_id = "test123"
# password = "password"
#
# con.execute('insert into Login values( %s,  %s)' % \
#             (user_id, password))
# # ..................................

#  创建窗体
cursor = db.cursor()
# cursor.execute('show databases')
# create1 =cursor.fetchall()
# print(create1)
# cursor.execute('create database zhengjie002')
# create2 = cursor.fetchall()
# print(create2)
cursor.execute('use zhengjie002')
# d = "create table anzhuo(ueser int(11))"
# cursor.execute(d)
cursor.execute('show tables')
f = cursor.fetchall()
print(f)

cursor.execute("insert into anzhuo value(1),(2),(3)")
db.commit()
cursor.execute("select ueser from anzhuo")
h = cursor.fetchall()
print(h)


