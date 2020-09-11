def parse_request(request_data, ip_port):
    """解析请求报文，返回客户端资源路径"""
    # 根据客户端浏览器请求的资源路径，返回请求资源
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

    # 9、拼接响应的报文
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server:Python20WS/2.1\r\n"
    response_blank = "\r\n"

    try:
        # 通过 with open 读取文件
        with open(resource_path, "rb") as file:
            # 把读取的文件内容返回给客户端
            response_body = file.read()
    except Exception as e:
        # 1）重新修改响应行 为 404
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 2）响应的内容为错误
        response_body = "Error! (%s)" % str(e)
        # 3）把内容转换为字节码
        response_body = response_body.encode()

    response_data = (response_line + response_header + response_blank).encode() + response_body

    return response_data
