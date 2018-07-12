from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://sytest.54315.com")
driver.find_element_by_class_name("user").send_keys("13727086330")
driver.find_element_by_class_name("password").send_keys("qwe123")
driver.find_element_by_class_name("password").submit()
sleep(2)
above = driver.find_element_by_xpath("/html/body/header/ul/li[2]/i[1]")
ActionChains(driver).move_to_element(above).perform()
# driver.find_element_by_xpath('/html/body/header/ul/li[2]').click()
element = WebDriverWait(driver, 5, 0.5).until(
                      EC.presence_of_element_located((By.XPATH, "/html/body/header/ul/li[2]/p/a[2]"))
                      )
element.click()
sleep(5)
# cookies = driver.get_cookies()
# ucsid = cookies[0]['value']
# print(ucsid)
