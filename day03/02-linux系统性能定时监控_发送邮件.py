#!/home/demo/.Envs/1-basics-python3/bin/python3
# 1、定义函数，实现信息的显示和日志的保存
# 2、死循环，每隔一段时间显示一次
# 1、导入模块
import psutil
import datetime
import yagmail


def linux_monitor(time):
    """定义函数，实现硬件信息的获取"""
    # 2、定义变量保存CPU的使用率
    cpu_per = psutil.cpu_percent(interval=time)

    # 3、定义变量保存内存信息
    memory_info = psutil.virtual_memory()

    # 4、定义变量保存硬盘的信息
    disk_info = psutil.disk_usage("/")

    # 5、定义变量保存网络的信息
    net_info = psutil.net_io_counters()

    # 获取系统当前时间
    current_time = datetime.datetime.now().strftime("%F %T")

    # 6、拼接字符串显示
    log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|      监控时间      |  CPU使用率  |   内存使用率  |   硬盘使用率  |          网络收发量          |\n"
    log_str += "|                   | (共%d核CPU)  |  (总计%dG内存) | (总计%dG硬盘)|                            |\n" % (
        psutil.cpu_count(logical=False), memory_info.total / 1024 / 1024 / 1024, disk_info.total / 1024 / 1024 / 1024)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    log_str += "|%s|    %s%%   |    %s%%    |    %s%%    |   收:%s/发:%s  |\n" % (
        current_time, cpu_per, memory_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
    log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
    print(log_str)

    # 7、保存监控信息到日志文件
    f = open("log.txt", "a")
    f.write(log_str + "\n\n")
    f.close()

    # 判断 CPU超过80% 内存超过90%
    if cpu_per > 80 or memory_info.percent > 90:
        # 8、发送邮件
        ya_obj = yagmail.SMTP(user="icoderi@163.com", password="py123456", host="smtp.163.com")
        # 8.1、使用yagmail 对象发送邮件（指定收件人、邮件主题、发送的内容）
        # send(指定收件人、邮件主题、发送的内容) 发送邮件
        ya_obj.send("py_test@126.com", "[系统监控报告]", log_str)


def main():
    """程序的入口"""
    while True:
        linux_monitor(5)


# __name__ 值：
# 1） 如果 03-liunx系统定时监控_定时功能.py 文件被其他文件导入
#  此时 __name__ 指的就是 "03-liunx系统定时监控_定时功能"
# 2) 如果直接运行 "03-liunx系统定时监控_定时功能.py" 文件
#  此时 __name__ 值是 __main__


if __name__ == '__main__':
    main()
