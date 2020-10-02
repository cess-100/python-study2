def creat_http_response(status, response_body):
    # 9、拼接响应的报文
    response_line = "HTTP/1.1 %s\r\n" + status
    response_header = "Server:Python20WS/2.1\r\n"
    # response_header += "Content-Type: text/html\r\n"
    response_blank = "\r\n"

    response_data = (response_line + response_header + response_blank).encode() + response_body

    return response_data
