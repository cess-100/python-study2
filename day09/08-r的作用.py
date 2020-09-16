import re

# r的作用 让正则中的 \ 没有特殊含义（转义） 就是代表原声的 斜杠
# result = re.match("<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\\2></\\1>", "<html><h1>asdbj</h1></html>")
result = re.match(r"<([a-zA-Z0-9]+)><([a-zA-Z0-9]+)>.*</\2></\1>", "<html><h1>asdbj</h1></html>")

if result:
    print("匹配成功!")
    # 4、如果成功，获取匹配的结果
    print("匹配结果:", result.group())
else:
    print("匹配失败!")
