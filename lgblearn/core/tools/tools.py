# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""
Usage Of 'tools' :
"""

from __future__ import print_function
import time
import datetime
import math
import os
from dateutil.parser import parse
import logging
import shutil
import string

from components.sql_format import sql_format as _sql_format
from lgblearn._version import PMAC, PWIN


def _get_variable_name(x):
    """通过变量获取变量名

    :param x: 传入变量
    :return:

    >>> mm = 1
    >>> _get_variable_name(mm)
    'mm'
    """
    for k, v in globals().items():
        if v is x:
            return k


def run_time(t1, name="", is_print=True):
    """Performance test function, test run time.

    :param t1: Set the time of the breakpoint
    :param name: Set the name of the print
    :param is_print: True, Whether to print
    :return: Printed string content

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

    >>> date_range('2017-10-01', '2017-10-04')
    ['2017-10-01', '2017-10-02', '2017-10-03']
    >>> date_range('2017-10-01', '2017-10-04', contain=True)
    ['2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04']
    >>> date_range('2017-10-01', 3)
    ['2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04']
    >>> date_range('2017-10-01', -3)
    ['2017-09-28', '2017-09-29', '2017-09-30', '2017-10-01']
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


def file_num2size(num_size, h=True):
    """文件大小数值变为 MB 的显示

    :param num_size: 文件大小
    :param h: 是否 human 显示
    :return: {'value': 数值，'measure': 单位，'str': 字串, 'org_size': 原始大小}
    """
    measure_list = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    fsize = num_size

    i = 0
    while (fsize >= 1) and (i < len(measure_list)) and h:
        if fsize < 1024:
            break
        else:
            fsize = fsize / 1024.0
            i += 1

    i = min(i, len(measure_list) - 1)
    fsize = round(fsize, 2) if not isinstance(fsize, int) else fsize
    res_info = {'value': fsize,
                'measure': measure_list[i],
                'str': str(fsize) + measure_list[i],
                'org_size': num_size}
    return res_info


def get_file_size(file_path, h=True):
    """获取文件的大小

    :param file_path: 文件路径
    :param h: 是否human可读
    :return: {'value': 数值，'measure': 单位，'str': 字串}
    """
    # file_path = unicode(file_path, 'utf8')
    org_fsize = os.path.getsize(file_path)
    res_info = file_num2size(org_fsize, h=h)
    return res_info


def timestamp2time(timestamp):
    """把时间戳转化为时间: 1479264792 to 2016-11-16 10:53:12"""
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)


def get_file_createtime(file_path):
    """获取文件的创建时间"""
    # file_path = unicode(file_path, 'utf8')
    t = os.path.getctime(file_path)
    return timestamp2time(t)


def get_file_modifytime(file_path):
    """获取文件的修改时间"""
    # file_path = unicode(file_path, 'utf8')
    t = os.path.getmtime(file_path)
    return timestamp2time(t)


def get_file_accesstime(file_path):
    """获取文件的访问时间"""
    # file_path = unicode(file_path, 'utf8')
    t = os.path.getatime(file_path)
    return timestamp2time(t)


def count_lines(file_path):
    """Count the lines number of a file.

    :param file_path: file path
    :return: lines number
    """
    if PMAC:
        lines = int(os.popen('wc -l {0}'.format(file_path)).readlines()[0].split()[0])
    elif PWIN:
        lines = 0
        with open(file_path, 'rb') as f:
            while True:
                read_buffer = f.read(8388608)  # 8 * 1024 * 1024
                if not read_buffer:
                    break
                lines += read_buffer.count('\n')
    else:
        raise Exception
    return lines


def sql_format(sql, wrap_add=None, mode='none'):
    """Format the sql string.

    :param sql: The input sql
    :param wrap_add: Add some string to wrap a line, such as ',', 'and'
    :param mode: 'none', 'upper', 'lower'. key words lower(upper), no change.
    :return: Formatted sql string.
    """
    kwargs = {'sql': sql, 'wrap_add': wrap_add, 'mode': mode}
    return _sql_format(**kwargs)


def transpose(matrix):
    """转置矩阵 list

    :param matrix: matrix list
    :return: transpose matrix list

    >>> matrix = [[1, 1, 2], [2, 2, 1], [3, 3, 2], [3, 4, 5]]
    # [1, 1, 2]
    # [2, 2, 1]
    # [3, 3, 2]
    # [3, 4, 5]
    >>> transpose(matrix)
    [[1, 2, 3, 3], [1, 2, 3, 4], [2, 1, 2, 5]]
    # [1, 2, 3, 3]
    # [1, 2, 3, 4]
    # [2, 1, 2, 5]
    """
    return map(list, zip(*matrix))


def rotate(matrix):
    """旋转矩阵 list

    :param matrix: matrix list
    :return: rotate matrix list

    >>> matrix = [[1, 1, 2], [2, 2, 1], [3, 3, 2], [3, 4, 5]]
    # [1, 1, 2]
    # [2, 2, 1]
    # [3, 3, 2]
    # [3, 4, 5]
    >>> rotate(matrix)
    [[2, 1, 2, 5], [1, 2, 3, 4], [1, 2, 3, 3]]
    # [2, 1, 2, 5]
    # [1, 2, 3, 4]
    # [1, 2, 3, 3]
    """
    return map(list, zip(*matrix)[::-1])


def _list_str(list_v, len_v):
    temp = string.Template(' {${name}:${value}}')
    str_list = []
    for i, each in enumerate(len_v):
        str_list.append(temp.substitute(name=i, value=each))
    str_v = ''.join(str_list)
    return str_v.format(*list_v)


def print_matrix(matrix, res=False):
    """打印 matrix list

    :param matrix: matrix list
    :param res: 是否返回值
    :return: 根据 res
    """
    matrix_t = transpose(matrix)
    matrix_len = map(lambda x: max(map(lambda y: len(str(y)), x)) + 2, matrix_t)
    matrix_list = map(lambda x: _list_str(x, matrix_len), matrix)
    matrix_str = '\n'.join(matrix_list)
    if not res:
        print(matrix_str)
    else:
        return matrix_str


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
