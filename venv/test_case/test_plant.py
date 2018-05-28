#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from time import sleep
import datetime


class MyTest(unittest.TestCase):
    """种植计划模块"""

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

    def test_login(self):
        """测试13727086330账号登陆"""
        driver = self.driver
        self.login()
        title = driver.title
        self.assertEqual(title, "珍药材溯源系统")

    def test_addplan(self):
        """新增种植计划"""
        driver = self.driver
        self.login()
        driver.find_element_by_xpath("/html/body/section/menu/ul/li/ul/li[1]/a/span").click()
        driver.find_element_by_xpath("/html/body/section/section/div[2]/a[1]").click()
        driver.find_element_by_id("breedName").clear()
        driver.find_element_by_id("breedName").send_keys("金银花")
        driver.find_element_by_xpath('//*[@id="dataForm"]/ul/li[2]/input[1]').click()
        driver.find_element_by_name("seedWeight").send_keys("1000")
        driver.find_element_by_xpath('//*[@id="dataForm"]/ul/li[4]/input[2]').click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/input').click()
        Select(driver.find_element_by_name("manager")).select_by_index(5)
        driver.find_element_by_id('Add').click()
        alter = driver.find_element_by_xpath('/html/body/div[2]/div[2]/p').text
        print(alter)
        self.assertEqual(alter, "新建计划成功！")

    def test_addtask(self):
        """下达种植任务"""
        driver = self.driver
        self.login()
        driver.find_element_by_xpath("/html/body/section/menu/ul/li/ul/li[1]/a/span").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="Fixed"]/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td[1]/input').click()
        driver.find_element_by_id('allocatTask').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="currentCont1"]/input[4]').click()
        driver.find_element_by_xpath('//*[@id="dataForm"]/ul/li[7]/textarea').send_keys("今天进行除草任务")
        driver.find_element_by_name('startTime').send_keys(self.today)
        driver.find_element_by_name('endTime').send_keys(self.endday)
        driver.find_element_by_id('Confirm').click()
        sleep(1)
        # driver.find_element_by_xpath('/html/body/div[2]')
        # driver.current_window_handle
        result = driver.find_element_by_class_name('tishi').text
        print(result)
        # driver.find_element_by_xpath('//*[@id="btn_0"]').click()
        self.assertEqual(result, "下达任务成功！")

    def test_search(self):
        """种植计划查询功能"""

        driver = self.driver
        self.login()
        driver.find_element_by_xpath("/html/body/section/menu/ul/li/ul/li[1]/a/span").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="queryForm"]/ul/li[1]/input').send_keys('三七')
        driver.find_element_by_xpath('//*[@id="queryForm"]/ul/li[6]/input').click()
        sleep(1)
        result = driver.find_element_by_xpath('//*[@id="Fixed"]/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td[3]').text
        print(result)
        self.assertIn('三七', result)

    def test_finish_plant(self):
        driver = self.driver
        self.login()
        driver.find_element_by_xpath("/html/body/section/menu/ul/li/ul/li[1]/a/span").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="Fixed"]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/a[2]').click()
        sleep(1)
        driver.find_element_by_id('btn_0').click()
        sleep(1)
        result = driver.find_element_by_class_name('tishi').text
        print(result)
        self.assertEqual(result,"操作成功！")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
