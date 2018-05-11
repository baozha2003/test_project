import smtplib
from email.mime.text import MIMEText
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
# 发送邮件主题
subject = 'python email test'
# 发送的附件
file_new = './report/2018-05-11 15_25_08result.html'
sendfile = open(file_new, 'rb')
mail_body = sendfile.read()
sendfile.close()

msg = MIMEText(mail_body, 'html', 'utf-8')
msg = MIMEText('请查看附件内容！', 'plain', 'utf-8')
msg['Subject'] = Header("自动化测试报告", 'utf-8')

# att = MIMEText(sendfile,'base64','utf-8')
# att["Content-Type"] = "application/octet-stream"
# att["Content-Disposition"] = 'attachment;filename="2018-05-11 15_25_08result.html"'

# msgRoot = MIMEText('related')
# msgRoot['Subject'] = subject
# msgRoot.attach(att)
#
# # 编写Html类型的邮件正文
# msg = MIMEText('Hello', 'html', 'utf-8')
# msg['subject'] = Header(subject, 'utf-8')

# 定义发件人和收件人参数
msg['from'] = 'baozha2003@163.com'
msg['to'] = '185143666@qq.com'

# 链接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print('邮件发送成功email has send out !')
