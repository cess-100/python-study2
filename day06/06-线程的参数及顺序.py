# 1、 导入模块
import time
import threading


# 唱歌的函数
def sing(a, b, c):
    print("参数：", a, b, c)
    for i in range(5):
        print("正在唱歌......")
        time.sleep(0.5)


# 跳舞的函数
def dance():
    for i in range(5):
        print("正在跳舞........")
        time.sleep(0.5)


# 调用
if __name__ == '__main__':
    # 2、创建线程对象 threading.Thread
    # 在线程中，传递参数有三种方法：
    # 1、 使用元组传递  threading.Thread(target=xxx, args=(参数1,参数2,...))
    # thread_sing = threading.Thread(target=sing, args=(10, 100, 1000))

    # 2、 使用字典传递  threading.Thread(target=xxx, kwargs={"参数名": 参数值,...})
    # thread_sing = threading.Thread(target=sing, kwargs={"a": 10, "c": 1000, "b": 100})

    # 3、 混合使用元组和字典 threading.Thread(target=xxx, args=(参数1,参数2,...), kwargs={"参数名": 参数值,...})
    thread_sing = threading.Thread(target=sing, args=(10,), kwargs={"c": 1000, "b": 10})
    thread_dance = threading.Thread(target=dance)

    # 3、启动子线程
    thread_sing.start()
    thread_dance.start()
