#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
import unittest
import time


class MyTest(unittest.TestCase):
    """溯源系统测试"""
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://sytest.54315.com"

    def test_sy54315(self):
        """测试13727086330账号登陆"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys("13727086330")
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys("qwe123")
        driver.find_element_by_class_name("password").submit()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title, "珍药材溯源系统")

    def tearDown(self):
        self.driver.quit()

        if __name__ == "__main__":
            unittest.main()
