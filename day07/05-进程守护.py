import time
import multiprocessing


def work1():
    for i in range(10):
        print("正在运行 work1.....")
        time.sleep(0.5)


if __name__ == '__main__':

    process_obj = multiprocessing.Process(target=work1)

    # 设置线程的setDaemon(True)
    # 设置 process_obj 子进程守护主进程
    process_obj.daemon = True

    process_obj.start()

    time.sleep(2)
    print("我要死~!")

    # terminate() 终止子进程的执行
    process_obj.terminate()

    exit()
    print("xxxxxxx")
