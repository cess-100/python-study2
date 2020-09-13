import time
import multiprocessing


def work1(a, b, c):
    print("参数：", a, b, c)
    for i in range(10):
        print("正在运行 work1.....")
        time.sleep(0.5)


if __name__ == '__main__':
    # 参数的传递有三种方式：
    # 1）使用 args 传递元组
    # 2）使用 kwargs 传递字典
    # 3）混合使用 args 和 kwargs
    # process_obj = multiprocessing.Process(target=work1, args=(10, 100,1000))
    # process_obj = multiprocessing.Process(target=work1, kwargs={"c": 1000, "a": 10, "b": 100})
    process_obj = multiprocessing.Process(target=work1, args=(10,), kwargs={"c": 1000, "b": 100})
    process_obj.start()

    print("xxxxx")
