"""
思路：
    def myopen(file_name,file_model)

            上文（打开资源）
            yield
            下文（关闭资源）

装饰器装饰函数的步骤：
1. 导入模块 from contextlib import contextmanager
2. 开始装饰 @contextmanager
"""
from contextlib import contextmanager


@contextmanager
def myopen(file_name, file_model):
    print("进入上文")
    # 1.上文 打开文件
    file = open(file_name, file_model)

    # 2.返回资源
    yield file

    print("进入下文")
    # 3. 下文 关闭资源
    file.close()


with myopen("hello.txt", "r") as file:
    file_data = file.read()
    print(file_data)
