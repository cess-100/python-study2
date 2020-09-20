import re

# match 和 search的区别
# 1)match 从需要检测.group的字符串的开头位置匹配，如果失败返回 None
# 2)search 从需要检测的字符串中搜索满足正则的内容，有则返回match object对象
# result = re.match("hello", "xhello@163.com")
# result = re.search("hello", "xhello@163.com")

# 一、search的使用
result = re.search("\d+", "阅读次数:9999")

if result:
    print("匹配成功!")
    # 4、如果成功，获取匹配的结果
    print("匹配结果:", result.group())
    print(result.start())
    print(result.end())
    print(result.span())
else:
    print("匹配失败!")

# 二、findall("正则表达式", "待查找的内容") 搜索全部，返回值是个列表
result = re.findall("\d+", "阅读次数:9999,转发次数：6666,评论次数：38")

if result:
    print("匹配成功!")
    print("匹配结果:", result)
else:
    print("匹配失败!")

# 三、sub("正则表达式", "新的内容", "要替换的字符串")
# 字符串替换（按照正则，查找字符串并且替换为指定的内容）返回值，是替换后的字符串
# result = re.sub("\d+", "10000", "阅读次数:9999,转发次数：6666,评论次数：38")
str1 = """
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
"""
result = re.sub("<[^>]+>|&nbsp;| |\n", "", str1)

if result:
    print("匹配成功!")
    print("匹配结果:", result)
else:
    print("匹配失败!")


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


ret = re.sub(r"\d+", add, "python = 997")
print(ret)

# 四、split("正则表达式", "待拆分的字符串")  按照正则拆分字符串，返回值是一个列表
result = re.split(":| ", "info:hello@163.com zhangsan lisi")

if result:
    print("匹配成功!")
    print("匹配结果:", result)
else:
    print("匹配失败!")
