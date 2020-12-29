import threading
import time


def work1():
    for i in range(10):
        print("正在执行work1......", i)
        time.sleep(0.5)


if __name__ == "__main__":
    thread_work = threading.Thread(target=work1)

    # 线程守护：子线程守护主线程
    # setDaemon(True) 表示子线程就守护了主线程（主线程结束后，子线程也结束）
    thread_work.setDaemon(True)

    thread_work.start()

    # 睡眠2秒
    time.sleep(2)
    print("Game Over!!")
    # 让程序退出，主线程主动结束
    exit()
