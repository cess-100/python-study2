# 可变: 变量创建完成后，内存可以改变
# 列表和字典
import copy

# 可变类型的 浅拷贝 也会产生新的空间，能够保持各自的独立性
list1 = [1, 2, 3]
print("list1 = ", list1, id(list1))

# 拷贝：
# copy(变量) 产生副本，浅拷贝
list2 = copy.copy(list1)
print("list2 = ", list2, id(list2))

list3 = list1
list3.append(5)
print("list1 = ", list1, id(list1))
print("list2 = ", list2, id(list2))
print("list3 = ", list3, id(list3))


print("*"*20)


list1 = [1, 2, 3]
print("list1 = ", list1, id(list1))

# deepcopy(变量) 产生副本，深拷贝
list2 = copy.deepcopy(list1)
print("list2 = ", list2, id(list2))

# 修改list2
list1.append(7)
print("list1 = ", list1, id(list1))
print("list2 = ", list2, id(list2))

# 总结：简单可变类型的深拷贝，会产生新的空间，能够保持的各自的独立性
