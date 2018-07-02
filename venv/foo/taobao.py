# coding: utf-8
from selenium import webdriver
import time

# 1.创建浏览器对象
driver = webdriver.Firefox()
# 2.打开淘宝首页
driver.get('http://www.taobao.com')
# 3.找到搜索输入框
search_ele = driver.find_element_by_id('q')
# 4.输入搜索关键词
search_ele.send_keys(u'冰姨凉茶铺')
# 5.找到搜索按钮
search_btn = driver.find_element_by_class_name('btn-search')
# 6.点击按钮
search_btn.click()
# 打开文件
file_handle = open('shops.txt', 'wb+')
for i in range(1, 3):
    print
    '正在爬取第%s页数据.......' % i
    # 让浏览器滚动，加载数据
    for x in range(1, 11, 2):
        # 暂停1秒再开始滚动
        time.sleep(0.5)
        j = x / 10.0
        # %f float小数类型的占位符
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        # 执行js代码
        driver.execute_script(js)

    # 浏览器滚动结束之后，取出数据
    # 找到所有的class名称为info-cont的标签
    shops = driver.find_elements_by_class_name('info-cont')
    # for循环遍历列表，取出每一个商品信息
    for shop in shops:
        # 写入数据  编码
        file_handle.write(shop.text.encode('utf-8'))
        # 写入换行符
        # file_handle.write('\n\n')

    # 查找下一页
    next_page = driver.find_element_by_link_text('下一页')
    next_page.click()

# 关闭文件
file_handle.close()
