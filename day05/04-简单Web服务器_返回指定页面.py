import socket


def request_handler(new_client_socket, ip_port):
    """接收信息，并且做出响应"""
    # 7、接收客户端浏览器发送的请求协议
    request_data = new_client_socket.recv(1024)

    # 8、判断协议是否为空
    if not request_data:
        print("%s客户端已经下线!" % str(ip_port))
        new_client_socket.close()
        return

    # 根据客户端浏览器请求的资源路径，返回请求资源
    # 1）把请求协议解码，得到请求报文的字符串
    request_text = request_data.decode()
    # 2）得到请求行
    #    （1） 查找 第一个\r\n 出现的位置
    loc = request_text.find("\r\n")
    #    （2） 截取字符串，从开头截取到 第一个\r\n 出现的位置
    request_line = request_text[:loc]
    # print(request_line)
    # 3）把请求行，按照空格拆分，得到列表
    request_line_list = request_line.split(" ")
    # print(request_line_list)

    # 得到请求的资源路径
    file_path = request_line_list[1]
    print("[%s]正在请求:%s" % (str(ip_port), file_path))

    # 9、拼接响应的报文
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server:Python20WS/2.1\r\n"
    response_blank = "\r\n"

    # 通过 with open 读取文件
    with open("static" + file_path, "rb") as file:
        # 把读取的文件内容返回给客户端
        response_body = file.read()

    response_data = (response_line + response_header + response_blank).encode() + response_body

    # 10、发送响应报文
    new_client_socket.send(response_data)

    # 11、关闭当前连接
    new_client_socket.close()


def main():
    """主函数"""
    # 1、导入模块
    # 2、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3、设置地址重用
    #                                 当前套接字            地址重用         值True
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8888))
    tcp_server_socket.listen(128)

    # 6、接受客户端连接 定义函数 request_handler()
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print("新客户来了:", ip_port)
        # 调用功能函数处理请求并且响应
        request_handler(new_client_socket, ip_port)

    # 11、关闭操作
    # tcp_server_socket.close()


if __name__ == '__main__':
    main()
