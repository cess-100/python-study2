"""
1、判断是否已满
2、判断是否已经为空
3、取出队列中消息的个数
"""

import multiprocessing

queue = multiprocessing.Queue(3)
queue.put(1)
queue.put(2)
queue.put(3)

# 取值
value = queue.get()

# 1、判断是否已满
# queue.full() 判断队列是否已满， True 满   False 未满
isFull = queue.full()
print("isFull ---->", isFull)

value = queue.get()
# 3、取出队列中消息的个数
print("消息的个数：", queue.qsize())

value = queue.get()
# 2、判断是否已经为空  True 空  False 未空
isEmpty = queue.empty()
print("isEmpty --->", isEmpty)
