"""
迭代 ---》遍历
可迭代 ---》 可遍历

# 哪些是可遍历
# 列表 元组  字符串  字典  range()

# 哪些不可遍历
# 10    myclass
"""

# 可迭代（遍历）对象
for value in [1, 2, 3]:
    print(value)
print("--" * 20)

for value in (4, 5, 6):
    print(value)
print("--" * 20)

for value in "hello":
    print(value)
print("--" * 20)

for value in {"name": "王铁锤", "age": 38}:
    print(value)
print("--" * 20)

# 不可迭代（遍历）对象
# 'int' object is not iterable
for value in 10:
    print(value)
print("--" * 20)
