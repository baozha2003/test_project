#!/usr/bin/env python
# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest
from time import sleep


class MyTest(unittest.TestCase):
    """溯源系统测试"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://sytest.54315.com"

    def test_login(self):
        """测试13727086330账号登陆"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys("13727086330")
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys("qwe123")
        driver.find_element_by_class_name("password").submit()
        sleep(2)
        title = driver.title
        self.assertEqual(title, "珍药材溯源系统")

    def test_addplan(self):
        """新增种植计划"""
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys("13727086330")
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys("qwe123")
        driver.find_element_by_class_name("password").submit()
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
        driver.get(self.base_url)
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys("13727086330")
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys("qwe123")
        driver.find_element_by_class_name("password").submit()
        driver.find_element_by_xpath("/html/body/section/menu/ul/li/ul/li[1]/a/span").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="Fixed"]/table/tbody/tr/td[1]/div/table/tbody/tr[2]/td[1]/input').click()
        driver.find_element_by_id('allocatTask').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="currentCont1"]/input[4]').click()
        driver.find_element_by_xpath('//*[@id="dataForm"]/ul/li[7]/textarea').send_keys("今天进行除草任务")
        driver.find_element_by_name('startTime').send_keys('2018-05-18')
        driver.find_element_by_name('endTime').send_keys('2018-05-25')
        driver.find_element_by_id('Confirm').click()
        sleep(1)
        # driver.find_element_by_xpath('/html/body/div[2]')
        # driver.current_window_handle
        alter = driver.find_element_by_class_name('tishi').text
        print(alter)
        # driver.find_element_by_xpath('//*[@id="btn_0"]').click()
        self.assertEqual(alter,"下达任务成功！")

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
        self.assertEqual(alter,'新建计划成功！')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
