from selenium import webdriver
from time import sleep
import os
import unittest


def login():
    clear = driver.find_element_by_class_name("user").clear()
    username = driver.find_element_by_class_name("user").send_keys("13727086330")
    clear2 = driver.find_element_by_class_name("password").clear()
    passwd = driver.find_element_by_class_name("password").send_keys("qwe123")
    submit = driver.find_element_by_class_name("password").submit()


driver = webdriver.Firefox()
driver.get('http://sytest.54315.com/')
login()
sleep(1)
driver.find_element_by_xpath('/html/body/section/menu/ul/li/ul/li[3]/a/span').click()
sleep(1)
elements = driver.find_element_by_name('file')
elements.click()
# elements[0].click()
sleep(1)
driver.find_element_by_xpath('//*[@id="reportForm"]/ul/li[1]/input').send_keys('马铃薯')
driver.find_element_by_xpath('//*[@id="time"]').send_keys('2018-06-20')
driver.find_element_by_xpath('//*[@id="reportForm"]/ul/li[4]/input').send_keys('干燥冷藏保存')
file_path = os.path.abspath('质检报告.jpg')
driver.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)
sleep(4)
driver.find_element_by_class_name('btn-green').click()
sleep(2)
# alter = driver.find_element_by_xpath('/html/body/div[1]/div[2]/p').text
# sleep(1)
# print(alter)
# unittest.TestCase.assertEqual(alter,'上传成功!')
sleep(30)
driver.quit()
