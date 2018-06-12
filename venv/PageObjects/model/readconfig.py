from configparser import ConfigParser
import time, sys
import codecs
import os


class ReadConfig(object):
    """docstring for hackTickets"""

    """读取配置文件"""

    def readConfig(self, config_file='config.ini'):
        print("加载配置文件...")
        # 补充文件路径，获得config.ini的绝对路径，默认为主程序当前目录
        # path = os.path.join(os.getcwd(), config_file)
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))+ '\%s' % config_file
        print(path)

        cp = ConfigParser()
        try:
            # 指定读取config.ini编码格式，防止中文乱码（兼容windows）
            cp.read_file(codecs.open(path, "r", "utf-8-sig"))
        except IOError as e:
            print(u'打开配置文件"%s"失败, 请先创建或者拷贝一份配置文件config.ini' % (config_file))
            input('Press any key to continue')
            sys.exit()
        # 登录名
        self.receive_email = cp.get("mail", "receive_email")
        # print(self.receive_email)
        self.receive_emails = self.receive_email.split(',')
        # print(self.receive_emails)
        self.chromedriver_location = cp.get("chromedriver", "chromedriver_location")
        # print(self.chromedriver_location)


if __name__ == '__main__':
    readConfig = ReadConfig()
    readConfig.readConfig()
