"""
1、定义要下载的图片路径
2、调用文件下载的函数，专门下载文件

文件下载函数
1、根据url地址请求网络资源
2、在本地创建文件，准备保存
3、读取网络资源数据 （循环）
4、把读取的网络资源写入到本地文件中
5、做异常捕获
"""
from gevent import monkey
monkey.patch_all()

import urllib.request
import gevent


def download_img(imgUrl, file_name):
    try:
        # 1、根据url地址请求网络资源
        response_data = urllib.request.urlopen(imgUrl)
        # 2、在本地创建文件，准备保存
        with open(file_name, "wb") as file:

            while True:
                # 3、读取网络资源数据 （循环）
                file_data = response_data.read(1024)
                # 判断读取的数据不为空
                if file_data:
                    # 4、把读取的网络资源写入到本地文件中
                    file.write(file_data)
                else:
                    break
    # 5、做异常捕获
    except Exception as e:
        print("文件%s下载失败！" % file_name)
    else:
        print("文件%s下载成功！" % file_name)


def main():
    # 1、定义要下载的图片路径
    img_url1 = "http://img.mp.itc.cn/upload/20170716/8e1b835f198242caa85034f6391bc27f.jpg"
    img_url2 = "http://img.mp.sohu.com/upload/20170529/d988a3d940ce40fa98ebb7fd9d822fe2.png"
    img_url3 = "http://image.uczzd.cn/11867042470350090334.gif?id=0&from=export"

    # 2、调用文件下载的函数，专门下载文件
    # download_img(img_url1, "1.gif")
    # download_img(img_url2, "2.gif")
    # download_img(img_url3, "3.gif")

    # 批量把 协程 给 join()
    # gevent.joinall([协程列表])
    gevent.joinall([
        gevent.spawn(download_img, img_url1, "1.gif"),
        gevent.spawn(download_img, img_url2, "2.gif"),
        gevent.spawn(download_img, img_url3, "3.gif")
    ])


if __name__ == '__main__':
    main()
