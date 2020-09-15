"""
1、创建一个生成器
    目标：实现斐波那契数列
    1） 定义变量保存第一列和第二列的值
    2） 定义变量保存当前生成的位置
    3） 循环生成数据，条件（当前的列数 < 总列数）
    4） 保存 a 的值
    5） 修改 a b 的值  （a = b, b = a+b）
    6)  当前列数 + 1
    7)  返回 a 的值 yield

2、定义变量保存生成器
next(生成器） 得到下一个元素值
"""


# 1、创建一个生成器
def fibnacci(n):
    # 目标：实现斐波那契数列
    # 定义变量保存第一列和第二列的值
    a = 1
    b = 1
    # 定义变量保存当前生成的位置
    current_index = 0
    print("------1111111----------")
    # 循环生成数据，条件（当前的列数 < 总列数）
    while current_index < n:
        data = a
        a, b = b, a + b
        current_index += 1

        print("---------22222-------")
        # 返回 a 的值 yield
        # 1, 充当retrurn 作用
        # 2, 保存程序的运行状态 并且暂停程序执行
        # 3, 当next 的时候，可以继续唤醒程序从yield位置继续向下执行
        yield data
        print("---------33333-------")


if __name__ == '__main__':

    # 2、定义变量保存生成器
    fib = fibnacci(5)

    # next(生成器） 得到下一个元素值
    value = next(fib)
    print("第1列", value)

    value = next(fib)
    print("第2列", value)

    value = next(fib)
    print("第3列", value)

    # value = next(fib)
    # print("第4列", value)
    #
    # value = next(fib)
    # print("第5列", value)
    #
    # value = next(fib)
    # print("第5列", value)
