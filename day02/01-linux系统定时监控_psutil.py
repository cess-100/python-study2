import psutil

# 获取CPU信息
# cpu的核心数
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
# cpu使用率
print(psutil.cpu_percent(interval=0.5))
# 获取每个核心的使用率
print(psutil.cpu_percent(interval=0.5, percpu=True))

# 获取内存信息
# 内存整体信息
print(psutil.virtual_memory())
# 内存使用率
print(psutil.virtual_memory().percent)

# 获取硬盘信息
# 硬盘分区信息
print(psutil.disk_partitions())
# 指定目录磁盘信息
print(psutil.disk_usage("/"))
# 硬盘使用率
print(psutil.disk_usage("/").percent)

# 获取网络信息
# 收到的数据包数量
print(psutil.net_io_counters().bytes_recv)
# 发送的数据包数量
print(psutil.net_io_counters().bytes_sent)

# 获取开机时间
print(psutil.boot_time()) # 1970年到现在的秒数

# 获取活动用户
print(psutil.users())
