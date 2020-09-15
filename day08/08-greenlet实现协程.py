"""
greenlet 实现协程的步骤：
1、导入模块
2、创建任务 work1   work2
3、创建 greenlet 对象
4、手动 switch 任务
"""

import time
from greenlet import greenlet


def work1():
    while True:
        print("正在执行work1...")
        time.sleep(0.5)

        # 切换到第二个任务
        g2.switch()


def work2():
    while True:
        print("正在执行work2................")
        time.sleep(0.5)

        # 切换到第一个任务
        g1.switch()


if __name__ == '__main__':

    # 创建greenlet的对象 greenlet(函数名)
    g1 = greenlet(work1)
    g2 = greenlet(work2)

    # 执行work1任务
    g2.switch()
