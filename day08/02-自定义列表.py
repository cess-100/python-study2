"""
1、MyList类
1）初始化方法
2）__iter__() 方法，对外提供迭代器
3）addItem() 方法，用来添加数据

2、自定义迭代器类：MyListIterator
1) 初始化方法
2) 获取下一个元素值的方法 __next__()

目标：
mylist = MyList()
for value in mylist:
    print(value)
"""


# MyList类
class MyList(object):
    # 1）初始化方法
    def __init__(self):
        # 定义实例属性，保存数据
        self.items = []

    # 2）__iter__() 方法，对外提供迭代器
    def __iter__(self):
        # 返回MyListIterator 对象
        return MyListIterator(self.items)

    # 3）addItem() 方法，用来添加数据
    def addItem(self, data):
        # 追加保存数据
        self.items.append(data)
        print(self.items)


# 2、自定义迭代器类：MyListIterator
class MyListIterator(object):
    # 初始化方法
    def __init__(self, items):
        # 定义实例属性，保存MyList类传递过来的items
        self.items = items

        # 记录迭代器迭代的位置
        self.current_index = 0

    # 获取下一个元素值的方法 __next__()
    # next(mylist_iterator) 就会调用 __next__() 方法
    def __next__(self):

        # 判断当前的下标是否越界
        if self.current_index < len(self.items):
            #     1）根据下标获取下标对应的元素值
            data = self.items[self.current_index]
            #     2）下标位置 +1
            self.current_index += 1
            #     3）返回下标对应的数据
            return data
        #  如果越界，直接抛出异常
        else:
            # raise 用于主动抛出异常
            # StopIteration 停止迭代
            raise StopIteration


if __name__ == '__main__':
    # 1、创建自定义列表对象
    mylist = MyList()
    mylist.addItem("张飞")
    mylist.addItem("关羽")
    mylist.addItem("刘备")
    mylist.addItem("曹操")

    # 遍历
    # 1) iter(mylist) 获取 mylist对象的迭代器  --> MyList --> __iter__()
    # 2）next(迭代器） 获取下一个值
    # 3）捕获异常
    for value in mylist:
        print("name:", value)

    mylist_iterator = iter(mylist)

    print(next(mylist_iterator))
    print(next(mylist_iterator))
    print(next(mylist_iterator))
    print(next(mylist_iterator))
    print(next(mylist_iterator))
