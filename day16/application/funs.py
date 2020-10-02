"""
定义若干函数，实现不同的功能
1. index()
2. center()
3. gettime()

装饰器路由：
1、装饰器工厂
2、待装饰函数
3、在装饰器的内部把路径添加到字典中
"""
import time
import re
from application import urls
import pymysql


def route(path):
    # path 向装饰器内部传递的参数   path   /index.py
    # 装饰器
    # 字典
    # {"index.py":index函数引用}

    def function_out(func):
        urls.route_dict[path] = func
        print("装饰[%s]" % path)

        def function_in():
            return func()

        return function_in

    return function_out


@route("/index.py")
# 1. route("/index.py")   ----> function_out 引用
# 2. @function_out
# 3. index = function_out(index)
#     index()             ----> function_in
def index():
    """ 处理 index.py 请求 """
    # 1. 打开本地网页文件
    with open("templates/index.html", "r", encoding="utf-8") as file:
        # 2. 读取文件内容
        content = file.read()

        # --- 数据库查询 -----
        # 1）导入模块
        # 2) 创建连接
        conn = pymysql.connect(host="localhost", database="stock_db", user="root", password="123123")
        # 3) 创建游标对象
        cur = conn.cursor()
        # 4）通过游标执行查询
        cur.execute("select * from info")
        # 5) 获取查询的结果
        # ((,,,,,,),(),())
        # data_from_myql = str(cur.fetchall())
        data_from_mysql = ""
        #  5.1 遍历元组（得到每一行信息）
        #  5.1 拼接html格式的字符串
        for line in cur.fetchall():
            str = """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
                    </tr>
                    """ % line
            data_from_mysql += str
        # 6) 关闭操作
        #    游标    连接
        cur.close()
        conn.close()

        # 3.导入正则模块
        # 4.使用 正则进行替换 {%content%} --> helloworld
        content = re.sub("{%content%}", data_from_mysql, content)

    # 5.返回文件内容
    return content


@route("/center.py")
def center():
    """ 处理 center.py 请求 """
    # 1. 打开本地网页文件
    with open("templates/center.html", "r", encoding="utf-8") as file:
        # 2. 读取文件内容
        content = file.read()

        # --- 数据库查询 -----
        conn = pymysql.connect(host="localhost", database="stock_db", user="root", password="123123")
        cur = conn.cursor()
        cur.execute(
            "select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info i inner join focus f on i.id = f.id")
        data_from_mysql = ""

        for line in cur.fetchall():
            str = """
                    <tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
                        <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>
                    </tr>
                    """ % line
            data_from_mysql += str
        # 6) 关闭操作
        #    游标    连接
        cur.close()
        conn.close()

        # 3.导入正则模块
        # 4.使用 正则进行替换 {%content%} --> helloworld
        content = re.sub("{%content%}", data_from_mysql, content)

    # 5. 返回文件内容
    return content


@route("/gettime.py")
def gettime():
    """ 处理 gettindexime.py 请求 """
    return "This is gettime show! %s " % time.ctime()
