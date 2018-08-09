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
    EC.presence_of_element_located((By.XPATH, "/html/body/header/ul/li[2]/p/a[1]"))
)
element.click()
# print(driver.current_window_handle)  # 输出当前窗口句柄（百度）
handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
# print(handles)
# sleep(2)
driver.switch_to_window(handles[1])
driver.find_element_by_id('Confirm').click()
# driver.find_elements_by_class_name()
# cookies = driver.get_cookies()
# ucsid = cookies[0]['value']
# print(ucsid)
