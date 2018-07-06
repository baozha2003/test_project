#!/usr/bin/env python
# -*- coding: utf_8 -*-

import xlrd
import requests
import re
import json

workbook = xlrd.open_workbook(r'E:\work\python case\learn\testcase.xls')
#根据路径打开excel文件
table = workbook.sheets()[0]
#获取第一个sheet
nrows = table.nrows
#获取行数
TestData = []
#数组
for i in range(1,nrows):
    TestData.append(table.cell(i,1).value)
    #循环数组末尾添加单元格数据
print(TestData)

for j in range(0,nrows-1):
    data = json.loads(TestData[j])
    #字符串转义json
    TestCase =data
    #循环数组赋值进入用例参数
    print(TestCase)
    #用例对应的参数
    results = requests.post('http://localhost:8081/swcw/back/sysLogin.action',data=TestCase)
    #post请求
    pattern = re.compile(r'toMain')
    #正则表达式 ps：我这个太简单了 o(︶︿︶)o 唉
    match = pattern.search(results.url)
    try:
        if results.status_code == 200:
            if match.group() == 'toMain':
                print('用例测试结果：测试通过')
        else:
            print('用例测试结果：请求失败')
    except AttributeError:
        print('用例测试结果：测试失败')