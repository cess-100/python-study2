# 1、导入模块
import socket

# 2、创建套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、建立连接
tcp_client_socket.connect(("www.icoderi.com", 80))

# 4、拼接请求协议
# 4.1 请求行
request_line = "GET / HTTP/1.1\r\n"
# 4.2 请求头
request_header = "Host:www.icoderi.com\r\n"
# 4.3 请求空行
request_blank = "\r\n"
# 整体拼接
request_data = request_line + request_header + request_blank

# 5、发送请求协议
tcp_client_socket.send(request_data.encode())

# 6、接收服务器响应内容
recv_data = tcp_client_socket.recv(4096)
# 解码
recv_text = recv_data.decode()

# 7、保存内容
# 7.1 查询 \r\n\r\n 的位置
loc = recv_text.find("\r\n\r\n")
# 7.2 截取字符串
html_data = recv_text[loc + 4:]
print(html_data)

# 7.3 保存内容到文件中
with open("index.html", "w") as file:
    file.write(html_data)

# 8、关闭连接
tcp_client_socket.close()
