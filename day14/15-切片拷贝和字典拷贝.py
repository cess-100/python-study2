
# 简单、可变 深拷贝
list1 = [1, 2, 3, 4, 5, 6, 7]

# 切片拷贝
list2 = list1[:]
print("list1 =", list1, id(list1))  # list1 = [1, 2, 3, 4, 5, 6, 7] 3131867685512
print("list2 =", list2, id(list2))  # list2 = [1, 2, 3, 4, 5, 6, 7] 3131867685576

print("*" * 10)

A = [1, 2, 3]
B = [11, 22, 33]
C = (A, B)

D = C[:]
print("C =", C, id(C))  # C = ([1, 2, 3], [11, 22, 33]) 3131875231560
print("D =", D, id(D))  # D = ([1, 2, 3], [11, 22, 33]) 3131875231560

print("*" * 10)

dict1 = {"age": [1, 2]}

dict2 = dict1.copy()
print("dict1 =", dict1, id(dict1))
print("dict2 =", dict2, id(dict2))

print("*" * 10)

dict1['age'][0] = 100
print("dict1 =", dict1, id(dict1))  # dict1 = {'age': [100, 2]} 1596361304536
print("dict2 =", dict2, id(dict2))  # dict2 = {'age': [100, 2]} 1596361304608
