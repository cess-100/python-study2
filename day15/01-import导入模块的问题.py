# import module1
#
# module1 -- 模块名
# name 模块module1 中的变量
# print(module1.name)


# 查看系统的path 环境变量
# 1) 导入模块 sys
# 2) sys.path 可以查看到环境变量的具体内容
import sys

for p in sys.path:
    print(p)

print('--' * 20)

# 把指定的路径加入到环境变量中
# 追加到末尾 有一个app1文件在桌面
# sys.path.append("G:\\Users\\huxiaowu\\Desktop")
# 追加到开头
sys.path.insert(0, "G:\\Users\\huxiaowu\\Desktop")

for p in sys.path:
    print(p)

import app1  # 得在添加路径的后面

print(app1.name)
