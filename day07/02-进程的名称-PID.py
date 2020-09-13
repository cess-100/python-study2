import time
import multiprocessing
import os
import threading


def work1():
    for i in range(10):
        print("正在运行 work1.....", multiprocessing.current_process())

        # 获取进程的编号
        print("子进程编号", multiprocessing.current_process().pid)
        print("正在运行 work1.....", os.getpid())

        # 获取进程的父id
        print("正在运行 work1.....", i, os.getpid(), "->父id", os.getppid())
        time.sleep(2)


if __name__ == '__main__':
    # 获取主进程的名称
    print(multiprocessing.current_process())
    print(threading.current_thread())

    # 获取进程的编号　process id ---> pid
    # 1) multiprocessing.current_process().pid 进程编号
    print("主进程编号:", multiprocessing.current_process().pid)
    # 2) 使用os模块来获取
    print("主进程编号：", os.getpid())

    # target 指定子进程要执行的分支函数
    # name   指定子进程的名称
    process_obj = multiprocessing.Process(target=work1, name="P1")
    process_obj.start()

    print("xxxxx")
