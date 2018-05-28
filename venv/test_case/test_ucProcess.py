#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from time import sleep
import datetime


class MyTest(unittest.TestCase):
    """初加工计划模块"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://sytest.54315.com"
        self.today = str(datetime.date.today())
        self.endday = str(datetime.date.today() + datetime.timedelta(days=7))

    def login(self):
        """测试13727086330账号登陆"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys("13727086330")
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys("qwe123")
        driver.find_element_by_class_name("password").submit()
        sleep(1)

    def test_addcjg(self):
        """新增初加工计划"""
        driver = self.driver
        self.login()
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

    def test_addcjgtask(self):
        """添加初加工任务"""
        driver = self.driver
        self.login()
        driver.find_element_by_xpath('/html/body/section/menu/ul/li/ul/li[2]/a/span').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/section/section/table/tbody/tr[2]/td[1]/input').click()
        driver.find_element_by_id('allocatTask').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="dataForm"]/ul/li[2]/input[2]').click()
        driver.find_element_by_xpath('//*[@id="dataForm"]/ul/li[3]/textarea').send_keys('今天进行药材清洗工作')
        driver.find_element_by_name('startTime').send_keys(self.today)
        driver.find_element_by_name('endTime').send_keys(self.endday)
        driver.find_element_by_id('Confirm').click()
        sleep(1)
        alter = driver.find_element_by_class_name('tishi').text
        print(alter)
        self.assertEqual(alter, "下达任务成功！")

    def test_search(self):
        """测试初加工任务搜索"""
        driver = self.driver
        self.login()
        driver.find_element_by_xpath('/html/body/section/menu/ul/li/ul/li[2]/a/span').click()
        sleep(1)
        driver.find_element_by_name('breedName').send_keys('金银花')
        driver.find_element_by_xpath('//*[@id="queryForm"]/ul/li[6]/input').click()
        sleep(1)
        result = driver.find_element_by_css_selector(
            'body > section > section > table > tbody > tr:nth-child(2) > td:nth-child(3)').text
        print(result)
        self.assertEqual(result, "金银花")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
