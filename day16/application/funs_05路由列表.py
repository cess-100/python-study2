"""
定义若干函数，实现不同的功能
1. index()
2. center()
3. gettime()
"""
import time


def index():
    """ 处理 index.py 请求 """
    return "This is index show!"


def center():
    """ 处理 index.py 请求 """
    return "This is center show!"


def gettime():
    """ 处理 index.py 请求 """
    return "This is gettime show! %s " % time.ctime()
