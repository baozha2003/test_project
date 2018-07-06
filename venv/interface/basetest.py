import requests
import xlrd
import json


def read_excel(file='api.xlsx'):
    data = xlrd.open_workbook(file)  # 打开excel读取文件
    table = data.sheet_by_index(0)  # 通过索引获取
    nrows = table.nrows  # 获取行数
    ncols = table.ncols  # 获取列数
    colnames = table.row_values(0)  # one rows data 获取整行
    list = []  # 建立一个空的数组
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                # row[i] = colnames[i] + row[i]
                app[colnames[i]] = row[i]
            list.append(app)
    return list


def test_login():
    url = "http://sytest.54315.com/login"
    querystring = json.loads(read_excel()[0]['params'])
    headers = {
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST", url, headers=headers, params=querystring)

    return response.text


if __name__ == '__main__':
    print(test_login())
