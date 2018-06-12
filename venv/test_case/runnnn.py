# coding=utf-8
import os
import time
from selenium import webdriver
import unittest
import HTMLTestRunner_PY3  # 导入HTMLTestRunner库，放在脚本的开头也是一样


class TestAuto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.get('http://www.xuanwo001.com')
        self.driver.find_element_by_class_name('el-checkbox__inner').click()  # 勾选不再提示
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="main-content"]/div/div[7]/div/i').click()  # 关闭活动页面
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/p').click()  # 点击登录按钮
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/h3/button[2]').click()  # 点击切换到密码登录
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[1]/div/div/input').send_keys('13266788131')
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[2]/div/div/input').send_keys('123456')
        time.sleep(1)
        self.driver.find_element_by_class_name('login-btn').click()  # 点击登录
        print(u'-------------------------------The test case Running start >>')

    def test_001(self):
        '''验证网址打开是否正确测试用例'''
        print(u'test_001>正常打开网址进入旋涡首页')
        self.assertEqual('https://www.xuanwo001.com/#/index', self.driver.current_url)
        print(u'>>>PASS')

    def tearDown(self):
        self.driver.quit()
        print(u'--------------------------------The test case End of Run >>')

    # def Suite(self):
    #     self.suiteTest = unittest.TestSuite()
    #     self.suiteTest.addTest(TestAuto("test_001"))
    #     return self.suiteTest


if __name__ == '__main__':
    # unittest.mian()
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestAuto("test_001"))
    # 确定生成报告的路径
    filePath = "pyResult.html"
    fp = open(filePath, 'wb')
    # 生成报告的Title,描述
    runner = HTMLTestRunner_PY3.HTMLTestRunner(stream=fp, title='Python TestReport',
                                               description='This  is Python  Report')
    # runner = unittest.TextTestRunner()
    runner.run(suiteTest)
    fp.close()
