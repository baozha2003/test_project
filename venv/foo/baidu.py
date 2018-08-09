from selenium import webdriver
from time import sleep
import unittest
import os


class test_baidu(unittest.TestCase):
    def test_baidu_title(self):
        dr = webdriver.Chrome()
        dr.maximize_window()
        dr.get('http://www.baidu.com')
        dr.find_element_by_id('kw').send_keys("远光")
        dr.find_element_by_id('kw').submit()
        sleep(1)
        self.assertEqual(dr.title, '远光_百度搜索')
        base_dir = os.path.dirname(__file__)
        file = base_dir + '/haha.png'
        # print(file)
        dr.get_screenshot_as_file(file)
        dr.quit()


if __name__ == '__main__':
    unittest.main()
