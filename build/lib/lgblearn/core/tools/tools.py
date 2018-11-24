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
import shutil


def run_time(t1, name="", is_print=True):
    """Performance test function, test run time.

    :param t1: Set the time of the breakpoint
    :param name: Set the name of the print
    :param is_print: True, Whether to print
    :return: Printed string content

    Examples
    --------
    >>> t1 = time.time()
    # test function
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


def mkdir(path, trash=False, clear=False, force=False):
    """Create folder，default：No folder, create folder; If there is a folder, do not do anything .

    :param str path: created path
    :param bool trash: True（original folder backup）indicate，If the folder exists，1、Rename the folder to '.Trash' 2、Create this folder
    :param bool clear: clear '.Trash' folder
    :param bool force: Force delete folder
    :return: None
    """

    if not os.path.exists(path):
        os.mkdir(path)
    elif trash:
        shutil.copytree(path, '.Trash')
        shutil.rmtree(path)
        os.mkdir(path)
    elif force:
        shutil.rmtree(path)
        os.mkdir(path)

    if clear:
        try:
            shutil.rmtree('.Trash')
        except:
            pass


def date_range(start_date, date_or_num, contain=False):
    """Specifies the start date and end date to get a date list. Uniform format, %Y-%m-%d.

    :param str start_date: start date, include
    :param date_or_num: end date(str) or date slide number
    :param contain: whether include the date
    :return: ( list<string> ) date list

    Examples
    --------
    >>> date_range('2017-10-01', '2017-10-04')
    ['2017-10-01', '2017-10-02', '2017-10-03']
    >>> date_range('2017-10-01', '2017-10-04', contain=True)
    ['2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04']
    >>> date_range('2017-10-01', 3)
    ['2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04']
    """
    start_date_dt = parse(start_date)
    if isinstance(date_or_num, (unicode, str)):
        end_date_dt = parse(date_or_num)
        if not contain:
            end_date_dt = end_date_dt - datetime.timedelta(1)
        if end_date_dt < start_date_dt:
            raise ValueError('start_date must less than end_date')
    elif isinstance(date_or_num, (float, int)):
        end_date_dt = start_date_dt + datetime.timedelta(date_or_num)
    else:
        raise ValueError('value type must be in (str, unicode, float, int)\n'
                         'Your value is : {0}({1})\n'.format(date_or_num, type(date_or_num)))
    min_date = min(start_date_dt, end_date_dt)
    max_date = max(start_date_dt, end_date_dt)

    date_list = map(lambda x: (min_date + datetime.timedelta(x)).strftime('%Y-%m-%d'),
                    range((max_date - min_date).days + 1))
    return date_list


# 待开发
def cp(from_path, to_path, is_dir=False):
    """复制文件（弃用 - 待修改）

    :param from_path: 原文件
    :param to_path: 复制后的文件
    """
    if is_dir:
        os.system(''' cp -rf {0} {1} ;'''.format(from_path, to_path))
    else:
        os.system(''' cp {0} {1} ;'''.format(from_path, to_path))


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
