# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""
Usage Of 'api' :
"""

import sys as sys

from tools.tools import *
from tools import npl as npl
from tools import pdl as pdl

from algorithms import algorithms as alg
from algorithms import maths as maths
from algorithms import eda as eda

# 获取函数名
_npl_funcs = ['npl.' + _f for _f in dir(npl) if
              (not _f.startswith('_')) and (_f not in sys.modules) and (_f not in ['np'])]
_pdl_funcs = ['pdl.' + _f for _f in dir(pdl) if
              (not _f.startswith('_')) and (_f not in sys.modules) and (_f not in ['pd'])]
_alg_funcs = ['alg.' + _f for _f in dir(alg) if
              (not _f.startswith('_')) and (_f not in sys.modules) and (_f not in ['np', 'pd', 'sm'])]
_maths_funcs = ['maths.' + _f for _f in dir(maths) if (not _f.startswith('_')) and (_f not in sys.modules)]
_eda_funcs = ['eda.' + _f for _f in dir(eda) if
              (not _f.startswith('_')) and (_f not in sys.modules) and (_f not in ['pd'])]

all_funcs = [_f for _f in dir() if
             (not _f.startswith('_')) and (_f not in sys.modules) and (_f not in ['npl', 'pdl', 'alg', 'maths'])] + \
            _npl_funcs + _pdl_funcs + _alg_funcs + _maths_funcs + _eda_funcs
