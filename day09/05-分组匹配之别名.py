import re

# \1 表示引用第1个分组
# \1   --> \ 有特殊用法
# \\   --> \
result = re.match("<(?P<name1>[a-zA-Z0-9]+)><(?P<name2>[a-zA-Z0-9]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>asdbj</h1></html>")

if result:
    print("匹配成功!")
    # 4、如果成功，获取匹配的结果
    print("匹配结果:", result.group())
else:
    print("匹配失败!")
