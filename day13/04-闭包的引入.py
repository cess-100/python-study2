def test():
    print("哈哈，我是一个寂寞的test！")


test()
# 函数名是一个特殊的变量
ret = test
print(ret)

# id() 获取对象地址
print("%x" % id(ret))
print("%x" % id(test))

# 通过ret调用函数
ret()

# 1.函数名是一个特殊的变量，保存了函数的地址
# 2.自定义一个变量可以获取函数地址
# 3.自定义变量调用函数   “变量名()”

"""
哈哈，我是一个寂寞的test！
<function test at 0x00000262CFEEC268>
262cfeec268
262cfeec268
哈哈，我是一个寂寞的test！
"""
