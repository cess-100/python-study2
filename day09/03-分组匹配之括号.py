# 1、导入模块
import re

# 2、通过 match 方法，验证正则
# result = re.match("^\w{4,20}@(163|126|sina|qq)\.com$", "hello@qq.com")
result = re.match("(\d{3,4})-(\d{7,8})", "010-12345678")

# 3、判断 验证是否成功
if result:
    print("匹配成功!")
    # 4、如果成功，获取匹配的结果
    print("匹配结果:", result.group())
    # print("提取子字符串:", result.group(1))
    print("提取区号:", result.group(1))
    print("提取电话号码:", result.group(2))

    print(result.start())
    print(result.end())
    print(result.span())
else:
    print("匹配失败!")
