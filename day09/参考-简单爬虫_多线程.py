"""

定义函数，实现获取影片地址 get_movie_link
1、设置爬去的电影列表页面
2、打开电影列表页，获取数据，并解码得到网页html文本内容
3、使用正则匹配获得 页面中的所有的影片名称和对应内容页连接
4、循环打开内容页，获取下载地址
5、保存影片名称和地址到字典中

定义主函数main 调用 get_movie_link 函数，获取地址

"""
import re
import urllib.request
import time
import threading


# 定义字典保存下载的影片信息
class Spider(object):

    def __init__(self):
        self.films_dict = {}
        self.i = 1
        self.lock1 = threading.Lock()

    def start(self):

        # 调用下载函数，获取下载连接
        for page in range(1, 3):
            t1 = threading.Thread(target=self.get_movie_link, args=(page,))
            t1.start()
        # 得到字典对应的数组
        list1 = self.films_dict.items()

        # 所有线程执行完毕后再退出
        while len(threading.enumerate()) != 1:
            time.sleep(1)

        # 遍历下载字典，获取影片名称、下载地址
        for film_name, film_download_url in list1:
            print(film_name, "|", film_download_url)


    def get_movie_link(self, page):

        # 1、设置爬去的电影列表页面
        film_list_url = "http://www.ygdy8.net/html/gndy/dyzz/list_23_%d.html" % page

        # 2、打开电影列表页，获取数据，并解码得到网页html文本内容
        # 2.1 打开列表页地址
        response_list = urllib.request.urlopen(film_list_url)
        # 2.2 得到列表页返回的数据
        response_list_data = response_list.read()
        # 2.3 解码数据
        response_list_text = response_list_data.decode("GBK")
        # 3、使用正则匹配获得
        url_list = re.findall("<a href=\"(.*)\" class=\"ulink\">(.*)</a>", response_list_text)

        # 页面中的所有的影片名称和对应内容页连接
        for film_content_url, film_name in url_list:

            # 4、循环打开内容页，获取下载地址
            film_content_url = "http://www.ygdy8.net"+film_content_url
            # 4.1 打开url地址，获取返回的数据
            response_content = urllib.request.urlopen(film_content_url)
            # 4.2 读取返回的数据
            response_data = response_content.read()
            # 4.3 解码数据
            response_content_text = response_data.decode("GBK")
            # 4.4 使用正则，取出下载地址
            ret = re.search("bgcolor=\"#fdfddf\"><a href=\"(.*?)\">",response_content_text)
            if ret:
                # 5、保存影片名称和地址到字典中
                self.lock1.acquire()
                self.films_dict[film_name] = ret.group(1)
                self.lock1.release()
                print("已经成功爬取%d个影片地址!" % self.i)
                self.i += 1
            else:
                continue


def main():

    film_spider = Spider()
    film_spider.start()


if __name__ == '__main__':

    main()

