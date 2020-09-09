"""
1、导入模块
2、创建套接字 TCP
3、建立连接  connect()
4、发送数据
5、关闭套接字
"""

# 1、导入模块
import socket

# 2、创建套接字 TCP
# socket.SOCK_STREAM  TCP传输方式
# socket.SOCK_DGRAM   UDP传输方式
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3、建立连接  connect()
# tcp_client_socket.connect(address)
# address --> ("ip", 端口)
tcp_client_socket.connect(("192.168.199.132", 8888))

# 4、发送数据
tcp_client_socket.send("约吗？".encode())

# 接收数据
recv_data = tcp_client_socket.recv(1024)
# recv_data 保存的是服务端回复的信息的二进制
# b'\xd4\xbc\xd4\xbc\xd4\xbc'
# 解码
recv_text = recv_data.decode()
print("收到数据:", recv_text)

# 5、关闭套接字
tcp_client_socket.close()
