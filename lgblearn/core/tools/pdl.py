# -*- coding:utf-8 -*-
"""
  Author  : 'longguangbin'
  Contact : lgb453476610@163.com
  Date    : 2018/11/21
  Usage   :
"""

import pandas as pd


def date_range(start_date, end_date, freq='D'):
    """返回日期函数。

    :param start_date: '2017-10-01' 开始日期
    :param end_date: '2017-11-01' 结束日期
    :param freq: 间隔频率
    :return: 日期 list

    ex:
    getDateRange(start_date, end_date, freq='D')
    getDateRange(start_date, end_date, freq='M')
    getDateRange(start_date, end_date, freq='H')
    """
    date_list = map(lambda x: str(x)[:10], pd.date_range(start_date, end_date, freq=freq).values)
    return date_list


def trans2str(data, cols):
    """
    讲num类型转化成str类型
    """
    for col in cols:
        data[col] = data.loc[:, [col]].applymap(str)
    return data


def trans2num(data, cols):
    """
    讲str类型转化成num类型
    """
    for col in cols:
        data[col] = data.loc[:, [col]].applymap(float)
    return data


def trans2int(data, cols):
    """
    讲str类型转化成int类型
    """
    for col in cols:
        data[col] = data.loc[:, [col]].applymap(int)
    return data


def cross_join(pda, pdb):
    pda['tmp_cross_join'] = '1'
    pdb['tmp_cross_join'] = '1'
    pdc = pda.merge(pdb, on=['tmp_cross_join'])
    pdc = pdc.drop(['tmp_cross_join'], axis=1)
    return pdc
