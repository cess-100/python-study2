"""
队列是multiprocessing 模块提供的一个类
1）创建队列（指定长度）
2）放值
3）取值
"""
import multiprocessing

# 1）创建队列（指定长度）
# multiprocessing.Queue(n)  n 表示队列长度
queue = multiprocessing.Queue(5)

# 2）放值
# queue.put(值)  向队列中放入值
queue.put(1)
queue.put("hello")
queue.put([1, 2, 3])
queue.put((4, 5, 6))
queue.put({"a": 10, "b": 100})

# 长度为5，放入第6个数据后，队列就进行入了阻塞状态，默认会等待队列先取出值再放入新的值
# queue.put(10)

# put_nowait() 表示放入值，如果已满，不再等待，直接报错
# queue.put_nowait(10)

# 3）取值
value = queue.get()
print(value)
print("--" * 20)

value = queue.get()
print(value)
print("--" * 20)

value = queue.get()
print(value)
print("--" * 20)

value = queue.get()
print(value)
print("--" * 20)

value = queue.get()
print(value)
print("--" * 20)

# ----------- 队列中已经没有值了-------
# 当队列已经空的时候，再次get() 程序进入阻塞状态，等待放入新的值到队列，然后再取
# value = queue.get()
# print(value)
# print("--"*20)

# get_nowait() 当队列已空的时候，不会等待放入新的值，直接报错
value = queue.get_nowait()
print(value)
print("--" * 20)
