#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: __init__.py.py
@time: 2017/11/15 下午5:25
"""


import os
from importlib import import_module


MODE = os.environ.get('MODE') or 'extcloud'

# MODE = os.environ
try:
    # print(('[√] 当前环境变量: %s' % MODE))
    current_config = import_module('config.' + MODE)
    print(('[√] 当前环境变量: %s' % MODE))
except ImportError:
    print ('[!] 配置错误，请初始化环境变量')
    print ('source env_develop.sh  # 开发环境')
    print ('source env_product.sh  # 生产环境')
