"""
yagmail 发送邮件：
1、导入模块
2、使用yagmail 的类创建对象（发件人、发件人授权码、发件的服务器）
3、使用yagmail 对象发送邮件（指定收件人、邮件主题、发送的内容）
"""

# 1、导入模块
import yagmail

# 2、使用yagmail 的类创建对象（发件人、发件人授权码、发件的服务器）
# 2.1 发件人： icoderi@163.com -->user="icoderi@163.com"
# 2.2 发件人授权码：password="py123456" 非密码，在邮箱设置
# 2.3 发件服务器： host="smtp.163.com"
ya_obj = yagmail.SMTP(user="icoderi@163.com", password="py123456", host="smtp.163.com")

# 3、使用yagmail 对象发送邮件（指定收件人、邮件主题、发送的内容）
content = "你好"

# send(指定收件人、邮件主题、发送的内容) 发送邮件
ya_obj.send("py_test@126.com", "测试一下", content)
