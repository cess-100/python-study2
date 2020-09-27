"""
类：  MyFile()
类方法：
    1. __enter__()  上文方法
    2. __exit__()   下文方法
    3. __init__()   方法，接收参数并且初始化

with MyFile('hello.txt', 'r') as file:
    file.read()
"""


class MyFile(object):

    # 1. __enter__()  上文方法
    def __enter__(self):
        print("进入上文....")
        # 1，打开文件
        self.file = open(self.file_name, self.file_model)
        # 2，返回打开的文件资源
        return self.file

    # 2. __exit__()   下文方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入下文....")
        # 关闭文件资源
        self.file.close()

    # 3. __init__()   方法，接收参数并且初始化
    def __init__(self, file_name, file_model):
        # 保存文件名和文件打开模式，到实例属性中
        self.file_name = file_name
        self.file_model = file_model


if __name__ == '__main__':

    with MyFile("hello.txt", "r") as file:
        # 开始读取文件
        file_data = file.read()
        print(file_data)

"""
进入上文....
hello,python!
进入下文....
"""