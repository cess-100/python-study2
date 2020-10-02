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
from application import urls


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
    return "This is index show!"


@route("/center.py")
def center():
    """ 处理 center.py 请求 """
    return "This is center show!"


@route("/gettime.py")
def gettime():
    """ 处理 gettindexime.py 请求 """
    return "This is gettime show! %s " % time.ctime()
