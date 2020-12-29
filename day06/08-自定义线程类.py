"""
1、让自定义类继承 threading.Thread 类
2、重写父类（threading.Thread） run方法
3、通过创建子类对象，让子类对象.start() 就可以启动子线程

threading.Thread():
    def start():
        self.run()

    def run():
        pass
"""
import threading
import time


# 自定义线程类 类名: MyThread
class MyThread(threading.Thread):

    def __init__(self, num):
        # 先去调用父类的init方法
        super().__init__()
        self.num = num

    # 重写 父类的run方法
    def run(self):
        for i in range(5):
            # self.name 从父类继承的一个属性
            print("正在执行子线程的run方法...", i, self.name, self.num)
            time.sleep(0.5)

    # def start():
    #    self run()


if __name__ == '__main__':
    # 创建对象
    mythread = MyThread(10)

    # 线程对象.start() 启动线程
    # 子类从父类继承了 start() 方法
    mythread.start()

    print("xxxxxx")
