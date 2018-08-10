import sys

sys.path.append('../db_fixture')
from venv.MysqlStu.mysql_db import DB

# 创建测试数据
datas = {
    'sign_guest': [
        {'id': 1, 'realname': 'alen', 'phone': 13727086333, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1},
        {'id': 2, 'realname': 'has sign', 'phone': 13727086222, 'email': 'sign@mail.com', 'sign': 0, 'event_id': 1}]
}

#将数据插入表
def init_data():
    db = DB()
    for table ,data in datas.items():
        db.clear()
        for d in data:
            db.insert(table,d)
    db.close()

if __name__ == '__main__':
    init_data()