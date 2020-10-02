# 1、导入模块
import socket
from application import app2


class WebServer(object):
    def __init__(self):
        # 2、创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server_socket.bind(("", 8888))
        self.tcp_server_socket.listen(128)

    def start(self):
        """启动Web服务器"""
        # 6、接受客户端连接 定义函数 request_handler()
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户来了:", ip_port)
            # 调用功能函数处理请求并且响应
            self.request_handler(new_client_socket, ip_port)

        # 11、关闭操作
        # tcp_server_socket.close()

    def request_handler(self, new_client_socket, ip_port):
        """接收信息，并且做出响应"""
        # 7、接收客户端浏览器发送的请求协议
        request_data = new_client_socket.recv(1024)

        # 8、判断协议是否为空
        if not request_data:
            print("%s客户端已经下线!" % str(ip_port))
            new_client_socket.close()
            return

        response_data = app2.application("static", request_data, ip_port)

        # 10、发送响应报文
        new_client_socket.send(response_data)

        # 11、关闭当前连接
        new_client_socket.close()


def main():
    """主函数"""
    # 创建WebServer类的对象
    ws = WebServer()
    # 对象.start() 启动Web服务器
    ws.start()


if __name__ == '__main__':
    main()
