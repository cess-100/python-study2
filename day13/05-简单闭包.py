def function_out(num):
    """外层函数"""
    print("1. function_out num=", num)

    def function_in(num_in):
        """里层函数"""
        print("2. ----- function_in ------num=", num)
        print("3. ----- function_in ------num_in=", num_in)

    return function_in


# function_out(10)
# 调用 function_out 获取内层函数的地址，保存到ret变量中
ret = function_out(100)

# 调用里层函数
ret(88)

"""
1. function_out num= 100
2. ----- function_in ------num= 100
3. ----- function_in ------num_in= 88
"""
