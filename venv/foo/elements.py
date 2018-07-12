# coding=utf-8


from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('http://news.baidu.com')

driver.implicitly_wait(8)

for i in driver.find_elements_by_xpath("//*/input[@type='radio']"):
    i.click()
