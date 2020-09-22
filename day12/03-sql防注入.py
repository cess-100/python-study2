import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123123', database='jing_dong')
cur = conn.cursor()

input_name = input("请输入要查询的名称:\n")
# 被注入的过程的分析：
# input_name = ' or 1 or '
# "select * from goods where name = '%s' order by id desc" % input_name
# "select * from goods where name = '' or 1 or '' order by id desc"
# 防止注入：
# 1）构建参数列表：params = [input_name]
# 2）把列表传递给 execute(sql, params)


params = [input_name]
sql ="select * from goods where name = %s order by id desc"
result = cur.execute(sql, params)

print("查询到:%s条数据" % result)
result_list = cur.fetchall()

for line in result_list:

    print(line)

cur.close()
conn.close()
