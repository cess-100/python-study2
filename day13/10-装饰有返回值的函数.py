def function_out(func):
    def function_in(num):
        print("------开始验证-------")
        return func(num)

    return function_in


@function_out
def login(num):
    print("开始登录！")
    return num + 10


# login(8) == function_in(8)
result = login(8)
print(result)
