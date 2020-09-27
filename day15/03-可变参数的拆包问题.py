# 定义两个函数  func02 func01
# func02 调用func01
# func02 有可变参数

def func01(*args, **kwargs):
    print("--------- func01 ---------")
    print("args =", args)
    print("kwargs =", kwargs)


def func02(*args, **kwargs):
    print("--------- func02 ---------")
    print("args =", args)
    print("kwargs =", kwargs)

    # 调用func01
    # 此处没有进行拆包，导致参数传递过去不不和要求
    func01(args, kwargs)
    func01(*args, **kwargs)


if __name__ == '__main__':
    func02(10, 20, 30, 40, 50, a=10, b=20)
