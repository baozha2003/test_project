# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self, user_name="xxx", pwd="xxx"):
        self.login("13727086330", "qwe123")

    def login(self, user_name, pwd):
        driver = webdriver.Firefox()
        driver.get("http://sytest.54315.com/")
        driver.find_element_by_class_name("user").clear()
        driver.find_element_by_class_name("user").send_keys(user_name)
        driver.find_element_by_class_name("password").clear()
        driver.find_element_by_class_name("password").send_keys(pwd)
        driver.find_element_by_class_name("password").submit()


if __name__ == "__main__":
    Login("13727086330", "qwe123")
