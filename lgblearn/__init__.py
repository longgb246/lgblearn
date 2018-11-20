# -*- coding:utf-8 -*-
"""
  Author  : 'longguangbin'
  Contact : lgb453476610@163.com
  Date    : 2018/11/18
  Usage   :
"""

# ------------------ origin learn the pandas init. ------------------

__docformat__ = 'restructuredtext'

# 检测是否有 hard dependencies 的缺失
# hard_dependencies = ('numpy', 'pytz', 'dateutil')
hard_dependencies = ('numpy', 'dateutil')
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(dependency)

if missing_dependencies:
    raise ImportError("Missing required dependencies {0}".format(missing_dependencies))
del hard_dependencies, dependency, missing_dependencies

# from core.api import *  # 会依次调用每个 module 下的 __init__.py 文件
# core __init__.py
# api __init__.py


from collections import ChainMap

values = ChainMap()
values['x'] = 3
values = values.new_child()
values['x'] = 2
print(values)
values = values.new_child()
print(values)
values['x'] = 1
print(values)
print(values['x'])
values = values.parents
print(values['x'])

