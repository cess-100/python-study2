"""
1、把 web服务器 返回值固定内容，代码拷贝过来
2、把原本固定的内容变为从数据库动态读取
1）导入pymysql 模块
2）连接数据库，并且查询所有的影片信息
3）遍历查询的结果集，拼接响应的主体

...发送给客户端....
"""

import pymysql
import socket


def request_handler(new_client_socket, ip_port):
    """接收信息，并且做出响应"""
    # 7、接收客户端浏览器发送的请求协议
    request_data = new_client_socket.recv(1024)
    # print(request_data)
    # 8、判断协议是否为空
    if not request_data:
        print("%s客户端已经下线!" % str(ip_port))
        new_client_socket.close()
        return

    # 9、拼接响应的报文
    # 9.1 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 9.2 响应头
    response_header = "Server:Python20WS/2.1\r\n"
    response_header += "Content-type:text/html;charset=utf-8\r\n"
    # 9.3 响应空行
    response_blank = "\r\n"
    # 9.4 响应的主体
    response_body = ""

    # 连接数据库，并且查询所有的影片信息
    conn = pymysql.connect(host="localhost", database="movie_db", user="root", password="123123")
    cur = conn.cursor()

    # 3）遍历查询的结果集，拼接响应的主体
    cur.execute("select * from movie_link order by id")
    result_list = cur.fetchall()

    for row in result_list:
        response_body += "%d.%s    下载地址:[<a href='%s'>%s</a>] <br>" % (row[0], row[1], row[2], row[2])
    # 关闭操作
    cur.close()
    conn.close()

    response_data = response_line + response_header + response_blank + response_body

    # 10、发送响应报文
    new_client_socket.send(response_data.encode())

    # 11、关闭当前连接
    new_client_socket.close()


def main():
    """主函数"""
    # 2、创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 3、设置地址重用
    #                                当前套接字            地址重用         值True
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 4、绑定端口
    tcp_server_socket.bind(("", 8888))
    # 5、设置监听，让套接字由主动变为被动接收
    tcp_server_socket.listen(128)

    # 6、接受客户端连接 定义函数 request_handler()
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()
        print("新客户来了:", ip_port)
        # 调用功能函数处理请求并且响应
        request_handler(new_client_socket, ip_port)


if __name__ == '__main__':
    main()
