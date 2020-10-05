"""
装饰器写法:
1. 存在闭包
2. 存在待修饰的函数
"""


def test(path):
    print(path)

    def function_out(func):
        """外层函数"""
        print("function_out path= ", path)

        def function_in():
            print("----开始验证----")
            func()

        # 返回内层函数的引用
        return function_in

    # 返回装饰器的引用
    return function_out


@test("login.py")
# @test("login.py") 分解为2步
# 1) test("login.py")  --> function_out 引用
# 2) @ 第一步的结果      --> @function_out
# 下一步：login = function_out(login)
def login():
    print("开始登录")


@test("register.py")
def register():
    print("开始注册")


register()
login()
