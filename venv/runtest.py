#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner

# 定义测试用例的目录为当前目录
test_dir = '../test_case/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = '../report/' + now + 'result.html'
    runner = unittest.TextTestRunner()

    # 定义报告存放路径
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况：')

    runner.run(discover)  # 运行测试用例
    fp.close()  # 关闭报告文件
