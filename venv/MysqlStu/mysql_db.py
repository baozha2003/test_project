from pymysql import  connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser

#读取db.config.ini文件设置
base_dir = str(os.path.dirname(__file__))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/db_config.ini"
print(file_path)