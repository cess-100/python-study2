"""
TCP服务端
1、导入模块
2、创建套接字
3、设置地址重用
4、绑定端口
5、设置监听，让套接字由主动变为被动接收
6、接受客户端连接 定义函数 request_handler()
7、接收客户端浏览器发送的请求协议
8、判断协议是否为空
9、拼接响应的报文
10、发送响应报文
11、关闭操作

"""
# 导入模块
import socket
from application import app2
import sys
import threading

"""
1、在类的初始化方法中配置当前当前的项目
{"2048":"./2048", "植物大战僵尸v1":"./zwdzjs-v1", ...}
2、给类增加一个初始化项目配置的方法 init_projects()
2.1  显示所有可以发布的游戏 菜单
2.2  接收用户的选择
2.3  根据用户的选择发布指定的项目 （保存用户选择的游戏对应的本地目录）
3、更改Web服务器打开的文件目录

"""


class WebServer(object):

    # 初始化方法
    def __init__(self, port):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.tcp_server_socket.bind(("", port))
        self.tcp_server_socket.listen(128)

        # 定义类的实例属性， projects_dict 初始化为空
        self.projects_dict = dict()

        # 定义实例属性，保存要发布的项目的路径
        self.current_dir = ""
        #                      key                    value
        self.projects_dict['植物大战僵尸-普通版'] = "zwdzjs-v1"
        self.projects_dict['植物大战僵尸-外挂版'] = "zwdzjs-v2"
        self.projects_dict['保卫萝卜'] = "tafang"
        self.projects_dict['2048'] = "2048"
        self.projects_dict['读心术'] = "dxs"

        # 调用初始化游戏项目的方法
        self.init_porjects()

    # 添加一个初始化项目的方法
    def init_porjects(self):
        # 2.1 显示所有可以发布的游戏菜单
        # list(self.projects_dict.keys()) 取出字典的key 并且强转为列表
        keys_list = list(self.projects_dict.keys())
        # 遍历显示所有的key
        # enumerate(keys_list)
        # [(0,'植物大战僵尸v1'), (1, '植物大战僵尸v2') ...]
        for index, game_name in enumerate(keys_list):
            print(index, ".", game_name)

        # 2.2 接收用户的选择
        sel_no = int(input("请选择要发布的游戏序号:\n"))

        # 2.3 根据用户的选择发布指定的项目 （保存用户选择的游戏对应的本地目录）
        #  根据用户的选择，得到游戏的名称（字典的key）
        key = keys_list[sel_no]
        #  根据字典的key 得到项目的具体路径
        self.current_dir = self.projects_dict[key]

    def start(self):
        """启动Web服务器"""
        print("Web服务器已经启动...等待客户端连接中....")
        # 6、接受客户端连接 定义函数 request_handler()
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print("新客户来了:", ip_port)

            # 创建线程
            thread_recvmsg = threading.Thread(target=self.request_handler, args=(new_client_socket, ip_port))

            # 设置线程守护
            thread_recvmsg.setDaemon(True)

            # 启动线程
            thread_recvmsg.start()

    def request_handler(self, new_client_socket, ip_port):
        """接收信息，并且做出响应"""
        # 7、接收客户端浏览器发送的请求协议
        request_data = new_client_socket.recv(1024)
        # print(request_data)

        # 8、判断协议是否为空
        if not request_data:
            print("%s客户端已经下线!" % str(ip_port))
            new_client_socket.close()
            return

        # 使用 application文件夹 app 模块的 application() 函数处理
        response_data = app2.application(self.current_dir, request_data, ip_port)

        # 10、发送响应报文
        new_client_socket.send(response_data)

        # 11、关闭当前连接
        new_client_socket.close()


def main():
    """主函数"""

    """
    1、导入sys 模块
    2、获取系统传递到程序的参数
    3、判断参数格式是否正确
    4、判断端口号是否是一个数字
    5、获取端口号
    6、在启动Web服务器的时候，使用指定的端口
    """

    # 判断参数格式是否正确
    if len(sys.argv) != 2:
        print("启动失败，参数格式错误!正确格式:python3 xxx.py 端口号")
        return

    # 4、判断端口号是否是一个数字
    #             0                     1
    # ['09-简单Web服务器_命令行启动.py', '8888']
    if not sys.argv[1].isdigit():
        print("启动失败，端口号不是一个纯数字!")
        return

    # 5、获取端口号
    port = int(sys.argv[1])

    # 6、在启动Web服务器的时候，使用指定的端口
    ws = WebServer(port)
    # 对象.start() 启动Web服务器
    ws.start()


if __name__ == '__main__':
    main()
