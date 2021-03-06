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
    unittest.main()
