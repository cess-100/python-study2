"""
1、导入模块
2、创建套接字
3、绑定端口
4、设置监听，设置套接字由主动为被动
5、接受客户端连接
6、接收客户端发送的文件名
7、根据文件名读取文件内容
8、把读取的内容发送给客户端（循环）
9、关闭和当前客户端的连接
10、关闭服务器
"""

# 1、导入模块
import socket

# 2、创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置套接字地址可以重用
# tcp_server_socket.setsockopt(当前套接字, 属性名, 属性值)
# socket.SO_REUSEADDR  地址是否可以重用   True可以重用  False 不可以重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 3、绑定端口
tcp_server_socket.bind(("", 8888))

# 4、设置监听，设置套接字由主动为被动
tcp_server_socket.listen(128)

# 5、接受客户端连接
while True:
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("欢迎新客户端:", ip_port)
    # 6、接收客户端发送的文件名
    recv_data = new_client_socket.recv(1024)
    file_name = recv_data.decode()
    print(file_name)

    try:
        # 7、根据文件名读取文件内容
        with open(file_name, "rb") as file:
            # 8、把读取的内容发送给客户端（循环）
            while True:
                file_data = file.read(1024)
                # 判断是否读取到了文件的末尾
                if file_data:
                    # 发送文件
                    new_client_socket.send(file_data)
                else:
                    break
    except Exception as e:
        print("文件%s下载失败!" % file_name)
    else:
        print("文件%s下载成功" % file_name)

    # 9、关闭和当前客户端的连接
    new_client_socket.close()

# 10、关闭服务器
# tcp_server_socket.close()

