# 1、导入模块
import socket

# 2、创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3、绑定端口和ip
tcp_server_socket.bind(("", 8081))

# 4、开启监听（设置套接字为被动模式）
# listen() 作用设置 tcp_server_socket 套接字为被动监听模式，不能在主动发送数据
# 128 允许接受的最大的连接数，在windows 128 有效，但是在linux 此数字无效
tcp_server_socket.listen(128)

# 5、等待客户端连接
# accept() 开始接受客户端连接,程序会默认进入阻塞状态（等待客户端连接），如果由客户端连接后，程序自动自动解除阻塞
# recv_data 数据含有两部分 1）返回了一个新的套接字socket 对象 2) 客户端的ip地址和端口号 元组
while True:
    new_client_socket, client_ip_port = tcp_server_socket.accept()
    print("新客户端来了:%s" % str(client_ip_port))

    # 6、收发数据
    while True:
        # recv() 会让程序再次阻塞，收到信息后再接阻塞
        recv_data = new_client_socket.recv(1024)

        # 当接受到数据为 空 的时候，表示客户端已经断开连接了，服务端也要断开
        # if len(recv_data)!= 0:
        # b'xxxx'
        # 如果recv_data 非空即为真，否则为假
        if recv_data:
            recv_text = recv_data.decode("GBK")
            print("接收到[%s]的信息:%s" % (str(client_ip_port), recv_text))
        else:
            print("客户端已经断开连接!")
            break

    # new_client_socket.close() 表示不能再和当前的客户端通信了
    new_client_socket.close()

# 7、关闭连接
# tcp_server_socket.close() 表示程序不再接受新的客户端连接，已经连接的可以继续服务
tcp_server_socket.close()
