"""
1、导入模块 pymysql
2、建立连接对象 pymysql.connect()
3、创建游标对象
4、使用游标对象执行SQL语句
5、获取执行的结果
6、打印输出获取的内容
7、关闭游标对象
8、关闭连接对象
"""
# 1、导入模块 pymysql
import pymysql


# 2、建立连接对象 pymysql.connect()
# pymysql.connect()
# host 主机
# user 用户名
# password 密码
# database 指定数据库
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123123', database='jing_dong')

# 3、创建游标对象
cur = conn.cursor()

# 4、使用游标对象执行SQL语句
# cur.execute(sql语句)，返回值是影响的行数，如果是查询语句，此处返回值总记录数
result = cur.execute("select * from goods order by id desc")
print("查询到:%s条数据" % result)

# 5、获取执行的结果
# cur.fetchone() 从查询的结果中取出一条数据
# result_list = cur.fetchone()
# print(result_list)

#              ((),(),())
result_list = cur.fetchall()
for line in result_list:
    # line 一行 是一个元组
    print(line)

# 6、关闭游标对象
cur.close()
# 7、关闭连接对象
conn.close()
