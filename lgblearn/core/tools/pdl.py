# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""
Usage Of 'pdl' :
"""

import pandas as pd


def trans_type(data, cols, tran_type):
    """Trans pandas cols types

    :param data: pandas dataframe
    :param cols: cols list
    :param tran_type: transform type
    :return:
    """
    types_dict = {'str': str, 'int': int, 'float': float}
    type_v = types_dict.get(tran_type)
    if type_v:
        data[cols] = data.loc[:, [cols]].applymap(type_v)
    else:
        raise ValueError('trans_type must be in {0}'.format(types_dict.keys()))
    return data


# 弃用的函数
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
