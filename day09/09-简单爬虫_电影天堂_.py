"""
一、定义函数获取列表页的内容页地址 get_movie_links()
1、定义列表的地址 http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html
2、打开url地址，获取数据
3、解码获取到的数据
4、使用正则得到所有的影片内容也地址

二、主函数 main
"""
import urllib.request
import re


def get_movie_links():
    """获取列表页影片信息"""
    # 1、定义列表的地址
    # http: // www.ygdy8.net / html / gndy / dyzz / list_23_1.html
    film_list_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html"
    # 2、打开url地址，获取数据
    reponse_list = urllib.request.urlopen(film_list_url)

    # 2.1 通过read()读取网络资源数据
    response_list_data = reponse_list.read()

    # 3、解码获取到的数据
    response_list_text = response_list_data.decode("GBK", errors="ignore")
    # 4、使用正则得到所有的影片内容地址
    #  4.1 使用findall() 根据正则查找所有影片对应的内容页地址
    url_list = re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>", response_list_text)
    #  4.2 保存地址
    # url_list = [('/html/.......', 'xxx影片'),('/html/.......', 'xxx影片')]
    # print(url_list)

    #  定义一个字典，用于保存影片信息
    films_dict = {}

    #  4.3 循环遍历 url_list
    i = 1
    for content_url, film_name in url_list:
        # 拼接内容页地址
        content_url = "http://www.ygdy8.net" + content_url
        # print("影片名称:%s,内容页地址:%s" % (film_name, content_url))
        # 4.4 打开内容页地址

        response_content = urllib.request.urlopen(content_url)
        # 4.5 接收内容页数据
        # 4.6 读取网络资源
        try:
            response_content_data = response_content.read()
        except Exception as e:
            response_content_data = e.partial
        # 4.7 解码得到内容页的文本内容
        response_content_text = response_content_data.decode("GBK", errors="ignore")
        # 4.8 取出下载地http://www.ygdy8.net址
        # print(response_content_text)
        result = re.search(r"bgcolor=\"#fdfddf\"><a href=\"(.*?)\">", response_content_text)
        # print(result.group(1))

        # 字典
        # {"xxxx影片": "xxx地址"}
        films_dict[film_name] = result.group(1)
        print("已经获取%d条信息" % i)
        i += 1

    return films_dict


def main():
    """"""
    films_dict = get_movie_links()
    # print(films_dict)

    # 把字典遍历输出
    for film_name, film_link in films_dict.items():
        print("%s | %s" % (film_name, film_link))


if __name__ == '__main__':
    main()
