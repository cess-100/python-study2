import time
import threading


# 唱歌的函数
def sing():
    for i in range(5):
        print("正在唱歌....", threading.current_thread())

        time.sleep(0.5)


# 跳舞的函数
def dance():
    for i in range(5):
        print("正在跳舞........", threading.current_thread())
        time.sleep(0.5)


# 调用
if __name__ == '__main__':

    # 线程的名称  threading.current_thread() 当前的线程对象
    print(threading.current_thread())

    # threading.enumerate() 可以获取正在活跃的线程列表
    thread_list = threading.enumerate()
    print("1当前线程数量：", len(thread_list))

    # 1、 导入模块
    # 2、创建线程对象 threading.Thread
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)

    # threading.enumerate() 可以获取正在活跃的线程列表
    thread_list = threading.enumerate()
    print("2当前线程数量：", len(thread_list))

    # 3、启动子线程
    thread_sing.start()
    thread_dance.start()

    while True:
        thread_num = len(threading.enumerate())
        print("3当前线程数量：", thread_num)

        # 如果只剩下主线程就停止
        if thread_num <= 1:
            break

        time.sleep(0.5)
