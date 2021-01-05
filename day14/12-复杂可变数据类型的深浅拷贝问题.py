import copy

A = [1, 2, 3]
B = [11, 22, 33]
C = [A, B]  # [[1, 2, 3], [11, 22, 33]]

print("A =", A, id(A))
print("B =", B, id(B))
print("C =", C, id(C))
print("C[0] =", C[0], id(C[0]))

print("*" * 20)

# 对复杂可变类型进行浅拷贝
# D产生了新的空间
D = copy.copy(C)
print("D =", D, id(D))
print("D[0] =", D[0], id(D[0]))

# 修改A的
A[0] = 10
print("A =", A, id(A))
print("D[0] =", D[0], id(D[0]))

print("*" * 20)

A = [1, 2, 3]
B = [11, 22, 33]
C = [A, B]

print("A =", A, id(A))
print("B =", B, id(B))
print("C =", C, id(C))

print("*" * 20)

# 对C做深拷贝
D = copy.deepcopy(C)
print("D =", D, id(D))
print("D[0]=", id(D[0]), "C[0]=", id(C[0]), "A=", id(A))

A[0] = 10
print("A =", A, id(A))
print("D[0] =", D[0], id(D[0]))
