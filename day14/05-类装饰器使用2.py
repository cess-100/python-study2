# 装饰器类
class Test(object):

    def __init__(self, func):
        print("----init----方法")
        print("---func--", func)
        # func 是login函数的引用
        self.func = func

    def run(self):
        print("---正在疯跑---")

    def __call__(self, *args, **kwargs):
        print("----开始验证----")
        # 调用原来login的内容
        self.func()


@Test
# login = Test(login)
def login():
    print("开始登录...")


login()
