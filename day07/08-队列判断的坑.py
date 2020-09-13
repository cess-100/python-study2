import multiprocessing
import time

# 创建队列
queue = multiprocessing.Queue(3)
queue.put(1)
queue.put(1)
queue.put(1)

time.sleep(0.00001)
# 判断队列是否为空
isEmpty = queue.empty()
print("isEmtpy = ", isEmpty)
