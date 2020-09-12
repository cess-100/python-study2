"""
子线程创建的步骤：
1、导入模块 threading
2、使用threading.Thread() 创建对象（子线程对象）
3、指定子线程执行的分支
4、启动子线程 线程对象.start()
"""
import time
import threading


# 定义函数
def saySorry():
    print("对不起，我错了!")
    time.sleep(0.5)


# 调用函数（单线程方式）
if __name__ == '__main__':

    # 1、导入模块 threading
    for i in range(5):
        # 2、使用threading.Thread() 创建对象（子线程对象）
        # 3、指定子线程执行的分支
        thread_obj = threading.Thread(target=saySorry)

        # 4、启动子线程 线程对象.start()
        thread_obj.start()

    print("xxxx")
