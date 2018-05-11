#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner


class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search(self):
        """测试搜索unittest并返回正确值"""
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
    testunit.addTest(Baidu("test_baidu_search"))

    # 定义报告存放路径
    fp = open('./result.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='用例执行情况：')

    runner.run(testunit)  # 运行测试用例
    fp.close()  # 关闭报告文件
