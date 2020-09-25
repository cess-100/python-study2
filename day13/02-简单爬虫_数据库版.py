"""
思路：
1、定义专门的函数，负责保存数据 add_film()
    1) 定义SQL 准备插入数据
    2）执行SQL语句

2、定义专门函数，负责检测数据库中是否存在相同的数据 film_exist()
    1）定义sql 根据影片名称和地址 查询
    2）执行查询，并获取查询的记录数
    3）如果获取的记录数 > 0     return True
    4) 如果获取的记录数 = 0     return False

3、创建连接对象（全局）
4、创建游标对象（全局）
5、关闭操作
"""

import urllib.request
import re
import pymysql


def add_movie(movie_name, movie_link):
    """保存影片到数据库中"""
    # 1) 定义SQL 准备插入数据
    sql = "insert into movie_link values (null,%s,%s)"
    # 2）执行SQL语句
    ret = cur.execute(sql, [movie_name, movie_link])
    # 如果插入成功，给出提示
    if ret:
        print("保存成功！影片[%s]" % movie_name)


def movie_exist(movie_name, movie_link):
    """检测数据是否已经存在"""
    # 1）定义sql 根据影片名称和地址 查询
    sql = "select id from movie_link where movie_name=%s and movie_link=%s limit 1"
    # 2）执行查询，并获取查询的记录数
    ret = cur.execute(sql, [movie_name, movie_link])
    # 3) 如果获取的记录数 > 0     return True
    # 4) 如果获取的记录数 = 0     return False
    if ret:
        return True
    else:
        return False


def get_movie_links():
    """获取列表页影片信息"""
    # 1、定义列表的地址
    film_list_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html"
    # 2、打开url地址，获取数据
    reponse_list = urllib.request.urlopen(film_list_url)
    response_list_data = reponse_list.read()

    # 3、解码获取到的数据
    response_list_text = response_list_data.decode("GBK", errors="ignore")

    # 4、使用正则得到所有的影片内容地址
    # url_list = [('/html/.......', 'xxx影片'),('/html/.......', 'xxx影片')]
    url_list = re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>", response_list_text)

    #  定义一个字典，用于保存影片信息
    films_dict = {}

    #  4.3 循环遍历 url_list
    i = 1
    for content_url, film_name in url_list:
        # 拼接内容页地址
        content_url = "http://www.ygdy8.net" + content_url

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
        result = re.search(r"bgcolor=\"#fdfddf\"><a href=\"(.*?)\">", response_content_text)

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
    for movie_name, movie_link in films_dict.items():

        # 如果数据库存在相同数据，就不在插入
        if movie_exist(movie_name, movie_link):
            print("保存失败!影片:[%s]" % movie_name)
            continue

        # 调用 add_film 方法添加数据
        add_movie(movie_name, movie_link)


if __name__ == '__main__':

    # 3、创建连接对象 （全局）
    conn = pymysql.connect(host="localhost", user="root", password="123123", database="movie_db")
    # 4、创建游标对象（全局）
    cur = conn.cursor()

    # 调用爬去数据的主函数
    main()

    conn.commit()

    # 5、关闭操作
    cur.close()
    conn.close()
