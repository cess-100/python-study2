class Goods(object):
    """这是一个商品的类 Goods"""
    # 类属性
    goods_color = "白色"

    def __init__(self):
        # 实例属性
        self.org_price = 100
        self.discount = 0.7

    def set_price(self):
        """这是Goods类中定义的设置价格方法"""
        pass

    def __call__(self, *args, **kwargs):
        print("__call__ 方法被调用")

    def __str__(self):
        return "我是一个寂寞的对象"

    # def __del__(self):
    #     print("__del__ 正在执行")

    def __getitem__(self, item):
        print("key = ", item)

    def __setitem__(self, key, value):
        print("key = %s, value = %s" % (key, value))

    def __delitem__(self, key):
        print("要删除 key = ", key)


goods = Goods()

# 对象名()  会去调用对象的 __call__() 方法
goods()

# print 打印对象的时候，默认输出<__main__.Goods object at 0x7efe5e9e0a20>
# __str__() 可以重写此输出
print(goods)

# 通过__dict__ 获取对象信息,对象.__dict__返回字典
# {'org_price': 100, 'discount': 0.7}
print(goods.__dict__)

# 通过__dict__ 获取类的信息  类名.__dict__  返回值是一个字典
# {'__module__': '__main__', '__doc__': '这是一个商品的类 Goods', 'goods_color': '白色', '__init__': <function Goods.__init__ at 0x0000022FF2C43730>, 'set_price': <function Goods.set_price at 0x0000022FF2C436A8>, '__call__': <function Goods.__call__ at 0x0000022FF2C430D0>, '__str__': <function Goods.__str__ at 0x0000022FF2C437B8>, '__del__': <function Goods.__del__ at 0x0000022FF2C43840>, '__getitem__': <function Goods.__getitem__ at 0x0000022FF2C438C8>, '__setitem__': <function Goods.__setitem__ at 0x0000022FF2C43950>, '__delitem__': <function Goods.__delitem__ at 0x0000022FF2C439D8>, '__dict__': <attribute '__dict__' of 'Goods' objects>, '__weakref__': <attribute '__weakref__' of 'Goods' objects>}
print(Goods.__dict__)

# dict1 = {}
# dict1['a'] = 10

# goods['a']      调用 __getitem__方法
goods['a']

# goods['a'] = 10 调用 __setitem__   key,value
goods['a'] = 10

# del goods['a']  调用 __delitem__  key
del goods['a']
