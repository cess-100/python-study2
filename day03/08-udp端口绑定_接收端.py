# 1、导入模块
import socket

# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
# udp_socket.bind(("127.0.0.1", 8888))
# ip地址尽可能写为"",好处当计算机由多个网卡的时候，不同网卡的数据都能被接收
udp_socket.bind(("", 8888))

# 3、接收数据（二进制）
recv_data = udp_socket.recvfrom(1024)
# 4、解码数据，得到字符串
recv_text = recv_data[0].decode(encoding="UTF-8", errors="ignore")

# 5、发送数据
udp_socket.sendto("吃屎吧".encode(), ("192.168.199.132", 9999))

# 6、输出显示接收到的内容
print("来自：", recv_data[1], "的消息：", recv_text)
# 7、关闭套接字
udp_socket.close()
