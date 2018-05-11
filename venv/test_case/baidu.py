#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import unittest
import time
# from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner_PY3 import HTMLTestRunner


class MyTest(unittest.TestCase):
    """搜索关键字unittest并返回正确结果"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu(self):
        """搜索关键字unittest并返回正确结果"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # unittest.main()
    testunit = unittest.TestSuite()
    testunit.addTest(MyTest("test_baidu"))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = '../report/' + now + 'result.html'
    # 定义报告存放路径
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况：')

    runner.run(testunit)  # 运行测试用例
    fp.close()  # 关闭报告文件
