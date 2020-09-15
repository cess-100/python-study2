def fibnacci(n):
    a = 1
    b = 1
    current_index = 0
    print("------1111111----------")

    while current_index < n:
        data = a
        a, b = b, a + b
        current_index += 1

        print("---------22222-------")
        xxx = yield data
        print("收到参数:", xxx)
        print("---------33333-------")

        if xxx == 1:
            # 生成器中能使用return 让生成器结束
            return "哈哈，我是return !我能让生成器结束!"


if __name__ == '__main__':
    fib = fibnacci(5)

    value = next(fib)
    print("第1列", value)

    try:
        value = next(fib)
        print("第2列", value)

        value = fib.send(1)
        print("第3列", value)
    except Exception as e:
        print(e)
