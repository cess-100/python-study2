def function_out(func):
    # func == login
    def function_in(*args, **kwargs):
        print("-----开始验证----")
        print("function_in:args=", args)
        print("function_in:kwargs=", kwargs)

        func(*args, **kwargs)

    return function_in


# 登录函数
@function_out
# login = function_out(login)
def login(*args, **kwargs):
    print("开始登录")
    print("login:args=", args)
    print("login:kwargs=", kwargs)


# 装饰后，login == function_in
login(10, a=10)