# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""  
Usage Of 'eda' : 
"""

from __future__ import print_function

from lgblearn.core.tools.tools import get_file_size, count_lines, print_matrix


def _summary_files(file_path):
    size_v = get_file_size(file_path).get('str')
    lines_v = count_lines(file_path)
    return [size_v, str(lines_v), file_path]


def summary_files(files, res=False):
    # summary_files2(['/Users/longguangbin/Downloads/flag_20181125105020.csv', '/Users/longguangbin/Downloads/granu_split_20181125175310.csv', '/Users/longguangbin/Downloads/seasonal_label.csv'])
    info_list = [['SIZE', 'LINES', 'FILE']]
    if isinstance(files, str):
        info_list.append(_summary_files(files))
    if isinstance(files, list):
        for each in files:
            info_list.append(_summary_files(each))
    info_str = print_matrix(info_list, res=True)
    if not res:
        print(info_str)
    else:
        return info_str
