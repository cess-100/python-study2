class Goods(object):
    """这是一个商品的类 Goods"""

    def set_price(self):
        """这是Goods类中定义的设置价格方法"""
        pass

    def __del__(self):
        print("__del__ 正在执行")


# 1、类的描述信息
# 类名.__doc__
print(Goods.__doc__)  # 这是一个商品的类 Goods

# 2、对象方法的描述
# 对象名.方法名.__doc__
goods = Goods()
print(goods.set_price.__doc__)  # 这是Goods类中定义的设置价格方法

# 3、获取当前模块
print(goods.__module__)  # __main__

# 4、获取对象所属的类
print(goods.__class__)  # <class '__main__.Goods'>

# 5、删除对象会执行 对象的 __del__()
del goods  # __del__ 正在执行
