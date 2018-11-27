# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/27
"""  
Usage Of 'plot_components' : 
"""

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter


def log_format(x, pos):
    """ """
    x_int = int(x)
    if x_int > 0:
        return '$10^{0}$'.format(x_int)
    else:
        return '0'


def normal_format(x, pos):
    """ """
    return '{0}'.format(x)


dark_colors = ['#4C72B0', '#6AB27B', '#C44E52', '#FFA455', '#a27712', '#8172B2', '#797979']
