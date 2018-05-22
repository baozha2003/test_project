#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from time import sleep
import datetime


class MyTest(unittest.TestCase):
    """溯源系统测试"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://sytest.54315.com"

    def test_addcjg(self):
        """新增初加工计划"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys("13727086330")
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys("qwe123")
        driver.find_element_by_class_name("password").submit()
        driver.find_element_by_xpath('/html/body/section/menu/ul/li/ul/li[2]/a/span').click()
        driver.find_element_by_xpath('/html/body/section/section/div[2]/a[1]').click()
        sleep(1)
        driver.find_element_by_name('choose').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="searchTable"]/tbody/tr[1]/td[1]/input').click()
        Select(driver.find_element_by_name("syManager")).select_by_index(5)
        driver.find_element_by_id('Add1').click()
        alter = driver.find_element_by_xpath('/html/body/div[3]/div[2]/p').text
        print(alter)
        self.assertEqual(alter, '新建计划成功！')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
