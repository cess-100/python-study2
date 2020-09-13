import multiprocessing
import time

# 定义全局变量
g_num = 10


# work1     对全局变量累加
def work1():
    global g_num

    for i in range(10):
        g_num += 1

    print("----------work1--------", g_num)  # 20


# work2     读取全局变量的值：如果能读取到，说全局变量能共享，否则不能共享的
def work2():
    print("----------work2--------", g_num)  # 10


# 定义两个进程
if __name__ == '__main__':
    # 创建进程 由3步
    # 创建进程对象
    work1_process = multiprocessing.Process(target=work1)
    work2_process = multiprocessing.Process(target=work2)

    work1_process.start()
    work2_process.start()

    time.sleep(3)

    print("----------main--------", g_num)  # 10
