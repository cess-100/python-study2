"""
目标：1.txt
下载到：1下载.txt

1、导入模块
2、创建套接字
3、建立连接
4、接收用户输入的文件名
5、发送文件名到服务端
6、创建文件，并且准备保存
7、接收服务端发送的数据，保存到本地（循环）
8、关闭套接字
"""

# 1、导入模块
import socket

# 2、创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3、建立连接
tcp_client_socket.connect(("192.168.199.132", 8888))

# 4、接收用户输入的文件名
file_name = input("请输入要下载的文件名:\n")

# 5、发送文件名到服务端
tcp_client_socket.send(file_name.encode())

# 6、创建文件，并且准备保存
with open(file_name + "下载", "wb") as file:
    # 7、接收服务端发送的数据，保存到本地（循环）
    while True:
        file_data = tcp_client_socket.recv(1024)

        # 判断数据是否传送完毕
        if file_data:
            file.write(file_data)
        else:
            break

# 8、关闭套接字
tcp_client_socket.close()
