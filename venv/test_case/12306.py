from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/")
driver.find_element_by_id("username").send_keys("185143666@qq.com")

driver.find_element_by_id("password").send_keys("chaoxiong6650312")
sleep(20)
driver.find_element_by_id("loginSub").click()
sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ul/li[2]/a")
sleep(2)
driver.find_element_by_id("fromStationText").send_keys("汉口")
driver.find_element_by_id("toStationText").send_keys("襄阳")
driver.find_element_by_id("query_ticket").click()