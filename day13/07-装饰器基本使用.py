"""
目标给 login() 增加验证功能
而且还不能修改源代码
"""


def function_out(func):
    # func = login
    def function_in():
        print("------开始验证-------")
        # func() = login()
        func()

    return function_in


@function_out
# @function_out 装饰了login() 函数
# 底层：
# login = function_out(login)
def login():
    print("开始登录！")


# 通过闭包调用外层函数
# login = function_out(login)
# # login() = function_in();
login()
