from pymysql import connect, cursors
from pymysql.err import OperationalError
import os
import configparser as cparser

# 读取db.config.ini文件设置
base_dir = str(os.path.dirname(__file__))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"
print(file_path)

cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# 封装MySQL的基本操作
class DB:
    def __init__(self):
        try:
            # 连接数据库
            self.conn = connect(host=host,
                                user=user,
                                password=password,
                                db=db,
                                charset='utf8mb4',
                                cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("MySQL error %d: %s" % (e.args[0], e.args[1]))

    # 清除表数据
    def clear(self):
        # real_sql = "truncate table" + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.conn.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.conn.commit()

    # 插入表数据
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
            key = ','.join(table_data.keys())
            value = ','.join(table_data.values())
            read_sql = "INSERT INTO" + table_name + "(" + key + ") VALUES(" + value + ")"
            # print(read_sql)

            with self.conn.cursor() as cursor:
                cursor.execute(read_sql)

            self.conn.commit()

    # 关闭数据库
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB()
    table_name = "sign_guest"
    data = ""
    db.clear()
    db.insert(table_name, data)
    db.close()
