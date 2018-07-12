
# coding=utf-8


from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('http://www.w3school.com.cn/example/xmle/books.xml')

driver.implicitly_wait(8)

for i in driver.find_elements_by_xpath("/bookstore/book/title"):
    print(i.text())
