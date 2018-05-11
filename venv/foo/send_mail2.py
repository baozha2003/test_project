import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 发送邮件服务器
smtpserver = 'smtp.163.com'
# 发送邮箱用户/密码
user = 'baozha2003@163.com'
password = 'baozha2003'
# 发送邮箱
sender = 'baozha2003@163.com'
# 接收邮箱
receiver = '185143666@qq.com'


# 发送的附件
file_new = '../report/2018-05-11 15_25_08result.html'
sendfile = open(file_new, 'rb')
mail_body = sendfile.read()
sendfile.close()

# 创建一个带附件的实例
msg = MIMEMultipart()
# 定义发件人和收件人参数
msg['from'] = 'baozha2003@163.com'
msg['to'] = '185143666@qq.com'

# 发送邮件主题
subject = '测试报告'
msg['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
msg.attach(MIMEText('测试报告请查看附件', 'plain', 'utf-8'))

att = MIMEText(mail_body, 'base64', 'utf-8')
att["Content-Type"] = "application/octet-stream"
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att["Content-Disposition"] = 'attachment;filename="2018-05-11 15_25_08result.html"'
msg.attach(att)

# 链接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print('邮件发送成功email has send out !')
