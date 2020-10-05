import threading


# 定义函数   根据下标获取列表元素值
def get_value(index):
    #            0  1  2  3  4
    data_list = [1, 3, 5, 7, 9]
    # 上锁
    lock.acquire()

    # 判断下标位置是否正确
    if index >= len(data_list):
        print("下标越界!", index)

        # 解锁
        lock.release()
        return
    print(data_list[index])
    # 解锁
    lock.release()


# 创建10个线程，观察资源的等待状态
if __name__ == '__main__':

    # 创建一把锁
    lock = threading.Lock()

    # 循环创建10个线程
    for i in range(10):
        t1 = threading.Thread(target=get_value, args=(i,))
        t1.start()
