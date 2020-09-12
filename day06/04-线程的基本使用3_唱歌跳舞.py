# 1、 导入模块
import time
import threading


# 唱歌的函数
def sing():
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
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)

    # 3、启动子线程
    thread_sing.start()
    thread_dance.start()
