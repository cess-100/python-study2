class Foo:
    def get_bar(self):
        return 'laowang'

    BAR = property(get_bar)

    # 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
    # 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
    # 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
    # 第四个参数是字符串，调用 类名.属性.__doc__ ，此参数是该属性的描述信息


obj = Foo()
reuslt = obj.BAR  # 自动调用get_bar方法，并获取方法的返回值
print(reuslt)
