from application import utils
from application import urls
from application import funs
import time

print(urls.route_dict)


def parse_request(request_data, ip_port):
    """解析请求报文，返回客户端资源路径"""
    request_text = request_data.decode()
    loc = request_text.find("\r\n")
    request_line = request_text[:loc]
    request_line_list = request_line.split(" ")
    file_path = request_line_list[1]
    print("[%s]正在请求:%s" % (str(ip_port), file_path))

    # 设置默认首页
    if file_path == "/":
        file_path = "/index.html"

    return file_path


def application(current_dir, request_data, ip_port):
    # 调用 parse_request函数，解析请求协议，返回请求的资源路径
    file_path = parse_request(request_data, ip_port)

    # 定义变量保存资源路径
    resource_path = current_dir + file_path
    response_data = ""

    # 改进动态显示
    # 判断后缀
    # 让.py显示的内容和html显示的内容区分开
    # index.py
    if file_path.endswith(".py"):
        # 判断请求资源路径，根据不同的路径显示不同的类容
        # /index.py  是否 在 route_dict 字典中的出现
        if file_path in urls.route_dict:
            # 根据key值，去urls.route_dict中，获取值（函数引用）
            func = urls.route_dict[file_path]
            # 根据路由字典，获取函数的引用，执行该函数，返回执行的结果，
            # 保存到 response_body 变量中
            response_body = func()
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.creat_http_response("200 OK", response_body.encode())

        else:
            response_body = "Sorry Page Not Found! 404"
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.creat_http_response("404 Not Found", response_body.encode())

    else:
        try:
            # 通过 with open 读取文件
            with open(resource_path, "rb") as file:
                # 把读取的文件内容返回给客户端
                response_body = file.read()

            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.creat_http_response("200 OK", response_body)
        except Exception as e:

            # 2）响应的内容为错误
            response_body = "Error! (%s)" % str(e)
            # 3）把内容转换为字节码
            response_body = response_body.encode()

            response_data = utils.creat_http_response("404 Not Found!", response_body)

    return response_data
