import re

# 贪婪：满足正则的情况下，尽可能多的取内容   默认为贪婪模式
# 非贪婪：满足正则的情况下，尽可能少的取内容
# 把贪婪模式该为非贪婪模式，需要使用符号：?  在+ * ? {} 后面添加? 可以变成非贪婪
# result = re.match("aaa(\d+?)", "aaa123456")

str1 = """
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
"""

result = re.search('src=\"(.*?)\"', str1)

# 3、判断 验证是否成功
if result:
    print("匹配成功!")
    # 4、如果成功，获取匹配的结果
    print("匹配结果:", result.group())
    print("地址：", result.group(1))
else:
    print("匹配失败!")
