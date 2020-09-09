"""
一、功能
1、发送信息
2、接收信息
3、退出系统

二、框架的设计
1、发送信息 send_msg()
2、接收信息 recv_msg()
3、程序的主入口 main()
4、当程序独立运行的时候，才启动聊天器

三、实现步骤
1、发送信息 send_msg()
1) 定义变量接收用户与输入的接收方的IP地址
2）定义变量接收用户与输入的接收方的端口号
3)定义变量接收用户与输入的接收方的内容
4）使用socket的sendto() 发送信息

2、接收信息 recv_msg()
1) 使用socket 接收数据
2）解码数据
3）输出显示

3、主入口main()
1）创建套接字
2）绑定端口
3）打印菜单（循环）
4）接收用户输入的选项
5）判断用户的选择，并且调用对应的函数
6）关闭套接字
"""
import socket


def send_message():
    """返送信息的函数"""
    pass


def recv_msg():
    """接收信息的函数"""
    pass


def main():
    """程序主入口"""
    # 1）创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2）绑定端口
    udp_socket.bind(("", 6666))

    # 3）打印菜单（循环）
    while True:
        print('\n\n*****************************')
        print('*******   1、发送信息   *******')
        print('*******   2、接收信息   *******')
        print('*******   3、退出系统   *******')
        print('*****************************')

        # 4）接收用户输入的选项
        sel_num = int(input('请输入选项：\n'))

        # 5）判断用户的选择，并且调用对应的函数
        if sel_num == 1:
            print('您选择的是发送信息')
        elif sel_num == 2:
            print('您选择的是接收信息')
        elif sel_num == 3:
            print('系统正在退出中...')
            print('退出完成！')
            break
        else:
            print('选项输入错误，请重新输入')

    # 6）关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    # 程序独立运行的时候，才去启动聊天器
    main()
