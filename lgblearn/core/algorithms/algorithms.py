# -*- coding:utf-8 -*-
"""
  Author  : 'longguangbin'
  Contact : lgb453476610@163.com
  Date    : 2018/11/21
  Usage   :
"""

import pandas as pd
import statsmodels.api as sm
import numpy as np
import warnings

from lgblearn.core.tools import npl

warnings.filterwarnings('ignore')
lowess = sm.nonparametric.lowess


# 6.2 主类
class SmoothMethod(object):

    @staticmethod
    def Lowess(x, y, theta=3, frac=0.3, it=2, int_method=''):
        """Lowess Smooth

        :param x: list | np.array | pd.Series
        :param y: list | np.array | pd.Series
        :param theta: x times of error
        :param frac: Between 0 and 1. The fraction of the data used when estimating each y-value.
        :param it: The number of residual-based reweightings to perform.
        :param int_method: int methods '' | 'ceil' | 'floor' | 'int'
        :return: np.array
        """
        int_methods = {'ceil': np.ceil, 'floor': np.floor, 'int': np.int32}
        x = np.array(x)
        y = np.array(y)
        lowes = lowess(y, x, frac=frac, it=it, return_sorted=False)
        err = y - lowes
        std_err = np.std(err)
        choose = (np.abs(err) < theta * std_err)
        if int_method == '':
            result = np.where(choose, y, lowes)
        elif int_method in ['ceil', 'floor', 'int']:
            func = int_methods[int_method]
            result = np.where(choose, func(y), func(lowes))
        else:
            raise ValueError('''int_method Must Be One Of : '' | 'ceil' | 'floor' | 'int' ! ''')
        return result

    @staticmethod
    def EMSmooth(x, y, theta=2, threshold=10, int_method=''):
        """EM Smooth

        :param x: list | np.array | pd.Series
        :param y: list | np.array | pd.Series
        :param theta: x times of error
        :param threshold: only higher than this can be thought as abnormal value
        :param int_method: int methods '' | 'ceil' | 'floor' | 'int'
        :return: np.array
        """
        int_methods = {'ceil': np.ceil, 'floor': np.floor, 'int': np.int32}
        y = np.array(y, dtype=np.float64)
        y_sort = np.argsort(np.argsort(y)[::-1])
        data = np.array([x, y, y_sort, range(len(x))]).T
        data = npl.sort(data, [2])
        flag = True
        i = 0
        while flag:
            avg = np.nanmean(data[(i + 1):, 1])
            sigma = np.nanstd(data[(i + 1):, 1])
            if (data[i, 1] <= avg + theta * sigma) | (data[i, 1] <= threshold):
                flag = False
            data[i, 1] = np.nan
            i += 1
        data = npl.sort(data, [0])
        result = pd.Series(data[:, 1]).interpolate(limit=len(data) - 1, limit_direction='both').values[
            np.argsort(data[:, -1])]
        if int_method in ['ceil', 'floor', 'int']:
            func = int_methods[int_method]
            result = func(y)
        elif int_method != '':
            raise ValueError('''int_method Must Be One Of : '' | 'ceil' | 'floor' | 'int' ! ''')
        return result

    @staticmethod
    def smooth(df, group_columns, target_columns, smooth_method='lowess', theta=-1.0, frac=-1.0, it=-1.0,
               threshold=-1.0, int_method=''):
        """DataFrame Smooth Method include lowess and emsmooth

        :param df: DataFrame
        :param group_columns: column may contain different values which should treat individually
        :param target_columns: column containing values needed to be smoothed
        :param smooth_method:
        :param theta: x times of error
        :param frac: Between 0 and 1. The fraction of the data used when estimating each y-value.
        :param it: The number of residual-based reweightings to perform.
        :param threshold: only higher than this can be thought as abnormal value
        :param int_method: int methods '' | 'ceil' | 'floor' | 'int'
        :return: DataFrame
        """
        kwargs_map = {'lowess': [SmoothMethod.Lowess, {'theta': 3, 'frac': 0.3, 'it': 2, 'int_method': ''}],
                      'emsmooth': [SmoothMethod.EMSmooth, {'theta': 2, 'threshold': 10, 'int_method': ''}]}
        smooth_method = smooth_method.lower()
        if smooth_method in ['lowess', 'emsmooth']:
            func = kwargs_map[smooth_method][0]
            kwargs = kwargs_map[smooth_method][1]
            for each in kwargs.keys():
                tmp_arg = eval(each)
                kwargs[each] = tmp_arg if tmp_arg != -1 else kwargs[each]
        else:
            raise ValueError(''' smooth_method Must Be One Of : 'lowess' | 'emsmooth' ! ''')
        split_data = []
        for key, grouped in df.groupby(group_columns):
            for target in target_columns:
                grouped['smoothed_{0}'.format(target)] = func(range(len(grouped)), grouped[target], **kwargs)
            split_data.append(grouped)
        result = pd.concat(split_data, ignore_index=True)
        return result
