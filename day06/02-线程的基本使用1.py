import time


# 定义函数
def saySorry():
    print("对不起，我错了!")
    time.sleep(0.5)


# 调用函数（单线程方式）
if __name__ == '__main__':

    for i in range(5):
        saySorry()
