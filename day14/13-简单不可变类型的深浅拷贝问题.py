import copy

# 简单不可变的元组
tuple1 = (1, 2, 3)
print("tuple1 = ", tuple1, id(tuple1))

# 对简单不可变类型做浅拷贝
# 等价于  tuple2 = tuple1
tuple2 = copy.copy(tuple1)
print("tuple2 = ", tuple2, id(tuple2))

print("*" * 20)

tuple1 = (1, 2, 3)
print("tuple1 = ", tuple1, id(tuple1))

# 等价于  tuple2 = tuple1
tuple2 = copy.deepcopy(tuple1)
print("tuple2 = ", tuple2, id(tuple2))
