"""
1、导入模块
2、创建套接字 （UDP）
3、发送数据
4、关闭套接字
"""

# 1、导入模块
import socket

# 2、创建套接字 （UDP）
# socket.AF_INET  IPv4
# socket.SOCK_DGRAM UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3、发送数据
# udp_socket.sendto(要发送的数据的二进制格式, 对方IP和端口号)
# 参数一： 要发送的数据的二进制格式
# 字符串转换为 二进制格式：   字符串.encode() 把字符串转换为二进制
# 参数二： 对方IP和端口号 address类型
# 要求ip和端口号是一个元组：1）第一个元素字符串类型 ip地址   2）整数类型的端口号
udp_socket.sendto("helloworld!".encode(), ('192.168.199.132', 8080))

# 4、关闭套接字
udp_socket.close()
