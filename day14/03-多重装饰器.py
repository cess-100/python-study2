"""
1.创建一个装饰器，一个待装饰的函数
"""


# 定义一个让文字加粗的装饰器
def makeBold(func):
    def function_in():
        return "<b>" + func() + "</b>"

    return function_in


# 定义一个让文字倾斜的装饰器
def makeItalic(func):
    def function_in():
        return "<i>" + func() + "</i>"

    return function_in


@makeBold
def test():
    return "hello world-1"


@makeItalic
def test2():
    return "hello world-2"


@makeItalic
@makeBold
def test3():
    return "hello world-3"


print(test())   # <b>hello world-1</b>
print(test2())  # <i>hello world-2</i>
print(test3())  # <i><b>hello world-3</b></i>


