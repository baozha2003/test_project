from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
from splinter.browser import Browser
from configparser import ConfigParser
from selenium import webdriver
from time import sleep
import traceback
import time, sys
import codecs
import argparse
import os
import time


class ReadConfig(object):
    """docstring for hackTickets"""

    """读取配置文件"""

    def readConfig(self, config_file='config.ini'):
        print("加载配置文件...")
        # 补充文件路径，获得config.ini的绝对路径，默认为主程序当前目录
        path = os.path.join(os.getcwd(), config_file)

        cp = ConfigParser()
        try:
            # 指定读取config.ini编码格式，防止中文乱码（兼容windows）
            cp.read_file(codecs.open(config_file, "r", "utf-8-sig"))
        except IOError as e:
            print(u'打开配置文件"%s"失败, 请先创建或者拷贝一份配置文件config.ini' % (config_file))
            input('Press any key to continue')
            sys.exit()
        # 登录名
        self.receive_email = cp.get("mail", "receive_email")
        print(self.receive_email)
        self.receive_emails = self.receive_email.split(',')
        print(self.receive_emails)
        self.chromedriver_location = cp.get("chromedriver", "chromedriver_location")
        print(self.chromedriver_location)

    # def loadConfig(self):
    #     parser = argparse.ArgumentParser()
    #     parser.add_argument('-c', '--config', help='Specify config file, use absolute path')
    #     args = parser.parse_args()
    #     if args.config:
    #         # 使用指定的配置文件
    #         self.readConfig(args.config)
    #     else:
    #         # 使用默认的配置文件config.ini
    #         self.readConfig()

    def baidu_test(self):
        driver = webdriver.Chrome(executable_path=self.chromedriver_location)
        driver.get('http://www.baidu.com')
        sleep(2)
        driver.quit()

    def send_mail(self):
        # 发送邮件服务器
        smtpserver = 'smtp.163.com'
        # 发送邮箱用户/密码
        user = 'baozha2003@163.com'
        password = 'baozha2003'
        # 发送邮箱
        sender = 'baozha2003@163.com'
        # 接收邮箱
        receiver = self.receive_emails
        # 发送邮件主题
        subject = 'python email test'
        # 发送的附件
        file_new = 'config.ini'
        sendfile = open(file_new, 'rb')
        mail_body = sendfile.read()
        sendfile.close()

        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg = MIMEText('请查看附件内容！', 'plain', 'utf-8')
        msg['Subject'] = Header("自动化测试报告", 'utf-8')

        # 定义发件人和收件人参数
        msg['from'] = 'baozha2003@163.com'
        msg['to'] = self.receive_email

        # 链接发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('邮件发送成功email has send out !')


if __name__ == '__main__':
    readConfig = ReadConfig()
    readConfig.readConfig()
    readConfig.baidu_test()
    readConfig.send_mail()
