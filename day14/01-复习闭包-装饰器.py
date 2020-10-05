def test():
    print("-----test-----")


# test()
#
# ret = test
# # 调用 test
# ret()


"""
闭包结构：
1. 存在函数的嵌套关系
2. 内存可以使用外层的变量
3. 外层返回内层的引用
"""

# def function_out(num):
#     def function_in():
#         print("num = ",num)
#
#     return function_in
#
#
# ret = function_out(10)


def function_out(func):
    def function_in():
        print("-----开始验证-----")
        func()

    return function_in


# @闭包的外层函数
@function_out
def login():
    print("开始登录")


# login = function_out(login)
login()
