# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""
Usage Of '__init__' :
"""

# ------------------ origin learn the pandas init. ------------------

__docformat__ = 'restructuredtext'

# 检测是否有 hard dependencies 的缺失
# hard_dependencies = ('numpy', 'pytz', 'dateutil')
hard_dependencies = ('dateutil',)
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(dependency)

if missing_dependencies:
    raise ImportError("Missing required dependencies {0}".format(missing_dependencies))
del hard_dependencies, dependency, missing_dependencies

## from core.api import *  # 会依次调用每个 module 下的 __init__.py 文件
# core __init__.py
# api __init__.py

## 关键的一步，把 core 的 Dataframe 提前
# from pandas.core.api import *

from core.api import *
