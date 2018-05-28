from selenium import webdriver
import unittest
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
base_url = "https://w.wjx.top/m/23836239.aspx"
driver.get(base_url)
# driver.find_element_by_id('q1_0').send_keys("阮超雄")
# driver.find_element_by_id('q1_1').send_keys("1")
# driver.find_element_by_id('q1_2').send_keys("1")
# driver.find_element_by_id('q1_3').send_keys("1")

for i in range(2, 32):
    xpath = '//*[@id="div%r"]/div[2]/div[3]/span/a'%i
    print(xpath)
    driver.find_element_by_xpath(xpath).click()
    sleep(1)
