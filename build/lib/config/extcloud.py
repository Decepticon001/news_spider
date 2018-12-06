#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: extcloud.py
@time: 2017-12-11 00:16
"""


import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)+'/../')

# requests 超时设置
REQUESTS_TIME_OUT = (30, 30)

HOST_IP = '172.31.119.35'

# 数据库 MySQL
# 存储库
DB_MYSQL_STORE = {
    'host': HOST_IP,
    'user': 'root',
    'passwd': 'royasoft',
    'port': 3306,
    'db': 'scrapy_news'
}
SQLALCHEMY_DATABASE_URI_MYSQL_STORE = \
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
    (DB_MYSQL_STORE['user'], DB_MYSQL_STORE['passwd'], DB_MYSQL_STORE['host'], DB_MYSQL_STORE['port'], DB_MYSQL_STORE['db'])

# 业务库
DB_MYSQL_SERVICE = {
    'host': HOST_IP,
    'user': 'root',
    'passwd': 'royasoft',
    'port': 3306,
    'db': 'headline'
}
SQLALCHEMY_DATABASE_URI_MYSQL_SERVICE = \
    'mysql+mysqldb://%s:%s@%s:%s/%s?charset=utf8' % \
    (DB_MYSQL_SERVICE['user'], DB_MYSQL_SERVICE['passwd'], DB_MYSQL_SERVICE['host'], DB_MYSQL_SERVICE['port'], DB_MYSQL_SERVICE['db'])

SQLALCHEMY_DATABASE_URI_MYSQL = SQLALCHEMY_DATABASE_URI_MYSQL_STORE

SQLALCHEMY_POOL_SIZE = 5  # 默认 pool_size=5

# 缓存，队列
REDIS = {
    'host': HOST_IP,
    'port': 6379,
    'password': '123456'  # redis-cli AUTH 123456
}

# 若快验证码识别
RK_CONFIG = {
    'username': 'huihan',
    'password': '123457hH',
    'soft_id': '93676',
    'soft_key': '5d0e00b196c244cb9d8413809c62f9d5',
}

# 每天请求限制（200元==500000快豆）
RK_LIMIT_COUNT_DAILY = 925

# 队列保留 cookies 数量
COOKIES_QUEUE_COUNT = 5

# 分布式文件系统
WEED_FS_URL = 'http://%s:9333' % HOST_IP

# 图片 base 地址
IMG_BASE_URL = 'http://47.104.73.227:8001/'

# 优先级配置（深度优先）
PRIORITY_CONFIG = {
    'list': 600,
    'next': 500,
    'detail': 800,
}
