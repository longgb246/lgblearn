# -*- coding:utf-8 -*-
"""
  Author  : 'longguangbin'
  Contact : lgb453476610@163.com
  Date    : 2018/11/21
  Usage   :
"""

import numpy as np


def loc(np_array, cols):
    """按照cols的布尔序列选出array的某些行

    :param np_array:
    :param cols: [True, False] 组成的 list 或者 np.array
    :return:

    Example
    ----------
    >>> loc(test, test[:,-1] == 1)  # 抽出test最后一列为1的np.array
    """
    return np_array[np.where(cols)[0], :]


def sort(np_array, cols, ascending=[]):
    """按cols从小到大排列array的行数据

    cols 为 [3, 1] 数字组成的 list
    使用方法如下：
    sort(test, [3, 1])           # 按照test的第4列，第2列从小到大排序
    """
    if ascending == []:
        sort_data = np_array[:, cols[::-1]].T
    else:
        sort_data = ([map(lambda x: 1 if x else -1, ascending[::-1])] * np_array[:, cols[::-1]]).T
    return np_array[np.lexsort(sort_data), :]


def drop_duplicates(np_array):
    """去重

    使用方法如下：
    drop_duplicates(test)           # 去除test的重复的行
    """
    return np.array(list(set([tuple(x) for x in np_array])))
