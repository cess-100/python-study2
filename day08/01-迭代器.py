"""
1） 一个可迭代对象可以提供一个迭代器
2）可迭代对象--->iter(可迭代对象)  ---> next(迭代器)
               迭代器                下一个元素

迭代器特点：
1）记录遍历的位置
2）提供下一个元素的值（配合next()函数）

for循环的本质：
1）通过 iter(要遍历的对象) 获取要遍历的对象的迭代器
2）next（迭代器）获取下一个元素
3）帮我们捕获了 StopIteration 异常
"""
# 1、data_list1 是一个可迭代对象
data_list1 = [1, 3, 5, 7, 9]
# for value in data_list1:
#     print(value)

# 2、获取迭代器
l1_iterator = iter(data_list1)

# 3、根据迭代器，可以获取下一个元素
value = next(l1_iterator)
print(value)  # 1

value = next(l1_iterator)
print(value)  # 3

value = next(l1_iterator)
print(value)  # 5

value = next(l1_iterator)
print(value)  # 7

value = next(l1_iterator)
print(value)  # 9

value = next(l1_iterator)
print(value)  # 报错 StopIteration


# 自定义迭代器类，满足2点
# 1）必须含有 __iter__()
# 2) 必须含有 __next__()
class MyIterator(object):
    def __iter__(self):
        pass

    # 当 next(迭代器) 的时候，会自动调用该方法
    def __next__(self):
        pass
