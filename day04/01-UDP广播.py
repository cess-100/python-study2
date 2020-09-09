"""
1、导入模块
2、创建套接字
3、设置广播权限
4、发送数据
5、关闭套接字
"""
# 1、导入模块
import socket

# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 3、设置广播权限(套接字默认不允许发送广播，需要开启相关权限)
# PermissionError: [Errno 13] Permission denied
# udp_socket.setsockopt(套接字,属性,属性值)
# socket.SOL_SOCKET 当前的套接字
# socket.SO_BROADCAST 广播属性
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)

# 4、发送数据
# udp_socket.sendto("哈哈，打不过我吧~".encode(), ("255.255.255.255", 8080))
udp_socket.sendto("哈哈，打不过我吧~".encode(), ("192.168.150.255", 8080))

# 5、关闭套接字
udp_socket.close()
