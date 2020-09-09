# 1、导入模块
import socket

# 2、创建套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 3、发送数据
udp_socket.sendto("哈哈，我来了".encode(), ("192.168.150.30", 8080))
# 4、接收数据（二进制）
recv_data = udp_socket.recvfrom(1024)

# 5、解码数据，得到字符串
# 指定解码格式 encoding="UTF-8"
# errors="ignore" 解码失败，忽略错误
# errors="strict" 严格模式，解码失败，出错
# decode(encoding="UTF-8", errors="ignore")
recv_text = recv_data[0].decode(encoding="UTF-8", errors="ignore")

# 6、输出显示接收到的内容
print("来自：", recv_data[1], "的消息：", recv_text)
# 7、关闭套接字
udp_socket.close()
