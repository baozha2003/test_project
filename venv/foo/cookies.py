from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://sytest.54315.com")
driver.find_element_by_class_name("user").send_keys("13727086330")
driver.find_element_by_class_name("password").send_keys("qwe123")
driver.find_element_by_class_name("password").submit()
sleep(0.5)
cookies = driver.get_cookies()
ucsid = cookies[0]['value']
print(ucsid)
