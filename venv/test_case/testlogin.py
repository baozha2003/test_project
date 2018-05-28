from selenium import webdriver
import time


def login():
    clear = driver.find_element_by_class_name("user").clear()
    username = driver.find_element_by_class_name("user").send_keys("13727086330")
    clear2 = driver.find_element_by_class_name("password").clear()
    passwd = driver.find_element_by_class_name("password").send_keys("qwe123")
    submit = driver.find_element_by_class_name("password").submit()


driver = webdriver.Firefox()
driver.get('http://sytest.54315.com/')
login()
