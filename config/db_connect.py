

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
    使用sqlalchemy连接数据库
"""

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'info'
MYSQL_USER = 'root'
MYSQL_PASSWD = '12341234'

#
# MYSQL_HOST = '47.104.73.227'
# MYSQL_DBNAME = 'headline'
# MYSQL_USER = 'root'
# MYSQL_PASSWD = 'royasoft'

engine=create_engine("mysql+pymysql://%s:%s@%s:3306/%s?charset=utf8"%(MYSQL_USER,MYSQL_PASSWD,MYSQL_HOST,MYSQL_DBNAME),echo=True)
DBSession = sessionmaker(bind=engine)