"""
1、创建一把互斥锁
2、在使用资源前要锁定资源
3、使用完资源之后，要解锁资源

"""

# 看看work1线程对全局变量的修改，在work2中能否查看修改后的结果
import threading
import time

# 定义全局变量
g_num = 0


# work1
def work1():
    # 声明g_num是一个全局变量
    global g_num

    # 上锁
    lock1.acquire()
    for i in range(1000000):
        g_num += 1
    # 解锁
    lock1.release()

    print("work1----------", g_num)  # 10


# work2
def work2():
    # 声明g_num是一个全局变量
    global g_num

    # 上锁
    lock1.acquire()
    for i in range(1000000):
        g_num += 1
    # 解锁
    lock1.release()

    print("work2----------", g_num)  # ？


if __name__ == '__main__':

    # 1、创建一把互斥锁
    lock1 = threading.Lock()

    # 创建2个子线程
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    # 启动线程
    t1.start()
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    # 在t1和t2 线程执行完毕后在打印g_num
    print("main------------", g_num)  # ？
