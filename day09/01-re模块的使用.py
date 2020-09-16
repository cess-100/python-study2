"""
1、导入模块
2、通过 match 方法，验证正则
3、判断 验证是否成功
4、如果成功，获取匹配的结果
"""
# 1、导入模块
import re

# 2、通过 match 方法，验证正则
# re.match("正则表达式", "要验证/检测的字符串")
# match() 方法如果匹配成功，返回 match object 对象
# match() 方法如果匹配失败，返回 None
#        正则字符串    要检测的内容
result = re.match("\w{4,20}@163\.com$", "hello@163.com")

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
