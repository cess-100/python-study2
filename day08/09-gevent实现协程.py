"""
gevent 好处：能够自动识别程序中的耗时操作，在耗时的时候自动切换到其他的任务
1、导入模块
2、指派任务
"""
# 一般放到开头处
# 1、导入模块
from gevent import monkey

# 2、破解所有
monkey.patch_all()

import time
import gevent


def work1():
    while True:
        print("正在执行work1...", gevent.getcurrent())
        time.sleep(0.5)
        # 默认情况下 time.sleep() 不能被gevent 识别为耗时操作
        # 1. 把time.sleep() ----> gevent.sleep()
        # gevent.sleep(0.5)

        # 2. 给　gevent 打补丁（目的：让　gevent 识别　time.sleep()）
        # 打补丁：
        # 　　在不修改程序源代码的情况下，为程序增加新的功能
        # 如何打补丁？
        # 1) 导入模块　monkey 模块　　　from gevent import monkey
        # 2) 破解　monkey.patch_all()


def work2():
    while True:
        print("正在执行work2................", gevent.getcurrent())
        time.sleep(0.5)
        # gevent.sleep(0.5)


if __name__ == '__main__':
    # 指派任务
    # gevent.spawn(函数名, 参数1,参数2,....)
    g1 = gevent.spawn(work1)
    g2 = gevent.spawn(work2)

    # 让主线程等待携程执行完毕再退出
    g1.join()
    g2.join()
