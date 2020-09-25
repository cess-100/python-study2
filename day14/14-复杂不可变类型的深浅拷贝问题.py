import copy

A = [1, 2, 3]
B = (11, 22, 33)
C = (A, B)
print("C =", C, id(C))

# 复杂不可变类型的浅拷贝
# 等价于 D = C
D = copy.copy(C)
print("D =", D, id(D))
print("D[0]", id(D[0]), "C[0]", id(C[0]), "A", id(A))

C[0][0] = 10
print("D = ", D, id(D))

print("*" * 10)

A = [1, 2, 3]
B = (11, 22, 33)
C = (A, B)

# 对C做深拷贝
D = copy.deepcopy(C)
print("C =", C, id(C))
print("D =", D, id(D))
print("D[0]", id(D[0]), "C[0]", id(C[0]), "A", id(A))  # D[0] 1742835782216 C[0] 1742835782024 A 1742835782024
print("D[1]", id(D[1]), "C[1]", id(C[1]), "B", id(B))  # D[1] 1742835455104 C[1] 1742835455104 B 1742835455104

# D拷贝自C,也是不可变的，D[0] 是一个列表，是可变的，通过D[0][0] 修改值
D[0][0] = 10
print("D =", D, id(D))
print("C =", C, id(C))

print("*" * 10)

A = (1, 2, 3)
B = (11, 22, 33)
C = (A, B)
D = copy.deepcopy(C)
print("C =", C, id(C))  # C = ((1, 2, 3), (11, 22, 33)) 2442508016136
print("D =", D, id(D))  # C = ((1, 2, 3), (11, 22, 33)) 2442508016136
