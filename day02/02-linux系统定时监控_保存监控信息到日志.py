import psutil
import datetime

# 定义变量保存信息
cpu_per = psutil.cpu_percent(interval=0.5)
memory_info = psutil.virtual_memory()
disk_info = psutil.disk_usage("/")
net_info = psutil.net_io_counters()
current_time = datetime.datetime.now().strftime("%F %T")

# 拼接字符串显示
log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (psutil.cpu_count(logical=False), memory_info.total/1024/1024/1024, disk_info.total/1024/1024/1024)
log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s   |\n" % (current_time, cpu_per, memory_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
print(log_str)

f = open("log.txt", 'a')
f.write(log_str + "\n\n")
f.close()
