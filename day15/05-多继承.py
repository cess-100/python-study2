# 定义父类Parent
class Parent(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        print('parent的init结束被调用')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        self.age = age
        # Parent.__init__(self, name)
        super(Son1, self).__init__(name, *args, **kwargs)
        print('Son1的init结束被调用')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        self.gender = gender
        # Parent.__init__(self, name)
        super(Son2, self).__init__(name, *args, **kwargs)
        print('Son2的init结束被调用')


# 定义子类  Grandson --继承--> Son1 \ Son2
class Grandson(Son1, Son2):
    def __init__(self, name, age, gender):
        # Son1.__init__(self, name, age)  # 单独调用⽗类的初始化方法
        # Son2.__init__(self, name, gender)
        super().__init__(name, age, gender)
        print('Grandson的init结束被调用')


# 创建对象
gs = Grandson('grandson', 12, '男')
print(Grandson.mro())
