"""
isinstance(待检测的对象, Iterable)
返回值为：True 可以迭代
        False 不可以迭代
"""
from collections import Iterable

ret = isinstance([1, 2, 3], Iterable)
print(ret)
print("--" * 20) # True

ret = isinstance((1, 2, 3), Iterable)
print(ret)
print("--" * 20) # True

ret = isinstance({"age": 18, "name": "铁锤"}, Iterable)
print(ret)
print("--" * 20) # True

ret = isinstance(100, Iterable)
print(ret)
print("--" * 20) # False


class MyClass(object):
    pass


myclass = MyClass()
ret = isinstance(myclass, Iterable)
print(ret)
print("--" * 20) # False


# 自定义一个类
class MyClass2(object):

    # 增加一个 __iter__方法
    # 该方法就是一个迭代器
    def __iter__(self):
        pass


myclass2 = MyClass2()
ret = isinstance(myclass2, Iterable)
print(ret)
print("--" * 20) # True

"""
1、可遍历对象就是可迭代对象
2、列表、元组、字典、字符串都是可迭代对象
3、100 和 自定义myclass 默认都是不可以迭代的
4、myclass 对象所属的类 MyClass 如果包含了 __iter__() 方法，此时myclass 就是一个可迭代对象
5、可迭代对象的本质：对象所属的类中包含了 __iter__() 方法
6、检测一个对象是否可以迭代，用 isinstance() 函数检测
"""
