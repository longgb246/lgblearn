# -*- coding:utf-8 -*-
"""
  Author  : 'longguangbin'
  Contact : lgb453476610@163.com
  Date    : 2018/11/21
  Usage   :
"""

import time
import datetime
import math
import os
from dateutil.parser import parse
import logging


def run_time(t1, name="", is_print=True):
    """性能测试函数，测试运行时间。

    :param t1: 设置断点的时间
    :param name: 设置打印的名称
    :param is_print: True, 是否打印
    :return: 打印的字符串内容

    Example
    ----------
    >>> t1 = time.time()
    # 测试的func
    >>> run_time(t1, 'name')
    """
    d = time.time() - t1
    min_d = math.floor(d / 60)
    sec_d = d % 60
    hor_d = math.floor(min_d / 60)
    if name != "":
        name = " ( " + name + " )"
    if hor_d > 0:
        v_str = '[ Run Time{3} ] is : {2} hours {0} min {1:.4f} s'.format(min_d, sec_d, hor_d, name)
    else:
        v_str = '[ Run Time{2} ] is : {0} min {1:.4f} s'.format(min_d, sec_d, name)
    if is_print:
        print(v_str)
    return v_str


def mkdir(path, trash=False, clear=True):
    """创建文件夹

    :param path:
    :param trash:  True， 表示，如果存在该文件夹，1、将该文件夹重命名为 .Trash 文件夹 2、在建立该文件夹
    :param clear:
    :return:
    """
    if not os.path.exists(path):
        os.mkdir(path)
    elif trash:
        os.system('''cp -rf {0}  .Trash '''.format(path))
        os.system('''rm -rf {0}  '''.format(path))
        os.mkdir(path)
    if clear:
        try:
            os.system('''rm -rf .Trash  ''')
        except:
            pass


def cp(from_path, to_path, is_dir=False):
    """复制文件（弃用 - 待修改）

    :param from_path: 原文件
    :param to_path: 复制后的文件
    """
    if is_dir:
        os.system(''' cp -rf {0} {1} ;'''.format(from_path, to_path))
    else:
        os.system(''' cp {0} {1} ;'''.format(from_path, to_path))


def date_range(start_date, end_date):
    """Specifies the start date and end date to get a date list. Uniform format, %Y-%m-%d.

    :param str start_date: start date, include
    :param str end_date: end date, not include
    :return: ( list<string> ) date list

    Example
    ----------
    >>> date_range('2017-10-01', '2017-10-04')
    ['2017-10-01', '2017-10-02', '2017-10-03']
    """
    start_date_dt = parse(start_date)
    end_date_dt = parse(end_date)
    date_list = map(lambda x: (start_date_dt + datetime.timedelta(x)).strftime('%Y-%m-%d'),
                    range((end_date_dt - start_date_dt).days))
    return date_list


def date_calculate(start_date, cal_date=0):
    """From the start date to a certain direction to get a date list.

    :param start_date: Start date to calculate
    :param cal_date: From the start date to a certain direction.
    :return: list

    Example
    ----------
    >>> date_calculate('2017-03-04', 3)
    ['2017-03-04', '2017-03-05', '2017-03-06', '2017-03-07']
    >>> date_calculate('2017-03-04', 0)
    ['2017-03-04']
    >>> date_calculate('2017-03-04', -3)
    ['2017-03-01', '2017-03-02', '2017-03-03', '2017-03-04']
    """
    start_date_dt = parse(start_date)
    end_date_dt = start_date_dt + datetime.timedelta(cal_date)
    min_date = min(start_date_dt, end_date_dt)
    max_date = max(start_date_dt, end_date_dt)
    date_list = map(lambda x: (min_date + datetime.timedelta(x)).strftime('%Y-%m-%d'),
                    range((max_date - min_date).days + 1))
    return date_list


class Logger(object):
    def __init__(self, logger=''):
        self.getOrCreate(logger)

    @staticmethod
    def _logger(mon_str):
        def wrapper_func(func):
            def wrapper_args(self, *args, **kwargs):
                self.logger.info('{0} ...'.format(mon_str))
                result = func(self, *args, **kwargs)
                self.logger.info('{0} Finish !'.format(mon_str))
                return result

            return wrapper_args

        return wrapper_func

    def _getLogger(self, logger):
        """取得log日志 """
        self.logger = logger

    def _setLogger(self):
        """设置log日志 """
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s (%(filename)s) [line:%(lineno)d] [ %(levelname)s ] %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            # filename='ModelSolve.log',
                            # filemode='w'
                            )
        self.logger = logging.getLogger("ModelClassify")

    def getOrCreate(self, logger=''):
        if logger == '':
            self._setLogger()
        else:
            self._getLogger(logger=logger)
