def function_out(func):
    # func == login
    def function_in(num):
        print("-----开始验证----,num = ", num)
        # func(num) == login(num)
        func(num)

    return function_in


# 登录函数
@function_out
# login = function_out(login)
def login(num):
    print("开始登录 num = ", num)


# 装饰后，login == function_in
login(10)
