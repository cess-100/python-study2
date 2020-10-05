import multiprocessing
import time


def copy_work():
    print("正在拷贝文件...", multiprocessing.current_process())
    time.sleep(0.5)


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)

    for i in range(10):
        # pool.apply(copy_work)
        pool.apply_async(copy_work)

    # close() 不再接收新的任务
    pool.close()

    # 让主进程等待进程池结束后在退出
    pool.join()
