# 导入模块
import socket

# 创建套接字，使用IPv4 UDP方式
# 参数一 协议类型：socket.AF_INET(IP4)   socket.AF_INET6(IP6)
# 参数二 传输方式：socket.SOCK_DGRAM(UDP)     socket.SOCK_STREAM(TCP)
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 数据的传递

# 关闭套接
tcp_socket.close()
