import time


def work1():
    while True:
        print("正在执行work1.....")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("正在执行work1........")
        yield
        time.sleep(0.5)


if __name__ == '__main__':
    w1 = work1()
    w2 = work2()

    while True:
        next(w1)
        next(w2)
