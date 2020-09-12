"""
1、导入模块
2、创建套接字
3、设置地址可以重用
4、绑定端口
5、设置监听，套接字有主动设置为被动
6、接受客户端连接
7、接收客户端发送的信息
8、解码数据并且进行输出
9、关闭和当前客户端的连接


"""
import socket
import threading


def recv_msg(new_client_socket, ip_port):
    while True:
        # 接收客户端发送的信息
        recv_data = new_client_socket.recv(1024)
        if recv_data:
            recv_text = recv_data.decode()
            print("收到来自[%s]的信息：%s" % (str(ip_port), recv_text))
        else:
            break

    new_client_socket.close()


tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp_server_socket.bind(("", 6666))
tcp_server_socket.listen(128)

while True:
    # 接受客户端连接
    new_client_socket, ip_port = tcp_server_socket.accept()
    print("新用户上线:", ip_port)

    # 创建线程
    thread_recvmsg = threading.Thread(target=recv_msg, args=(new_client_socket, ip_port))

    # 设置线程守护
    thread_recvmsg.setDaemon(True)

    # 启动线程
    thread_recvmsg.start()

# tcp_server_socket.close()
