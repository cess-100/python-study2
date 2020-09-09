# 1、导入模块
import socket

# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
# udp_socket.bind(address)
# address 是一个元组,元组的第一个元素是字符串类型的IP地址，第二个元素 整数端口号
# ip地址可以省略，省略后表示自己的ip地址
udp_socket.bind(("", 9999))

# 3、发送数据
udp_socket.sendto("哈哈，我来了".encode(), ("192.168.199.132", 8888))

# 4、接收数据（二进制）
recv_data = udp_socket.recvfrom(1024)

# 5、解码数据，得到字符串
recv_text = recv_data[0].decode(encoding="UTF-8", errors="ignore")

# 6、输出显示接收到的内容
print("来自：", recv_data[1], "的消息：", recv_text)

# 7、关闭套接字
udp_socket.close()
