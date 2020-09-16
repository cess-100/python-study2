# 1、导入模块
import re

# 2、通过 match 方法，验证正则
result = re.match("^[1-9]?[0-9]$|^100$", "66")

# 3、判断 验证是否成功
if result:
    print("匹配成功!")
    # 4、如果成功，获取匹配的结果
    print("匹配结果:", result.group())
    print(result.start())
    print(result.end())
    print(result.span())
else:
    print("匹配失败!")
