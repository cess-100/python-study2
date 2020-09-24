"""
目标：插入 100000 数据到  python_index_db 库中的 test_index 表
pymysql操作步骤：
1、导入模块
2、创建连接对象
3、创建游标对象
4、for循环，插入10万条数据
5、提交数据
6、关闭游标
7、关闭连接
"""

# 1、导入模块
import pymysql

# 2、创建连接对象
conn = pymysql.connect(host="localhost", database="python_index_db", user="root", password="123123")
# 3、创建游标对象
cur = conn.cursor()

# 4、for循环，插入10万条数据
for i in range(100000):
    cur.execute("insert into test_index(title) values('ha-%d')" % i)

# 5、提交数据
conn.commit()

# 6、关闭游标
cur.close()
# 7、关闭连接
conn.close()
