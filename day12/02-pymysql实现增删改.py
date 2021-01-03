"""
1、导入模块
2、创建连接对象
3、创建游标对象
4、使用游标对象执行SQL
5、提交
6、获取执行的结果（影响的行数）并打印执行的结果
7、关闭游标
8、关闭连接
"""
# 1、导入模块
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="123123", database="jing_dong")
cur = conn.cursor()

# 4、使用游标对象执行SQL
# sql = "insert into goods value (default, '老王牌拖拉机', 1, 1, 9998, 1, 1)"
# sql = "delete from goods where id = 24"
sql = "update goods set name = '最新款老王牌拖拉机' where id = 25"
ret = cur.execute(sql)

# 5、提交
# conn.commit() 提交刚刚执行的SQL
conn.commit()

# 6、获取执行的结果（影响的行数）
print("影响行数:", ret)

cur.close()
conn.close()
