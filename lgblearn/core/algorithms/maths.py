# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""
Usage Of 'maths' :
"""

import math
import copy


class Combine(object):
    """生成排列组合 """

    def __init__(self, arr_list=None):
        self.all_Tree = []
        self.tree_arrange_List = []  # 排列
        self.tree_combine_List = []  # 组合
        self.tree_q = 0
        arr_list = ['0'] if arr_list is None else arr_list
        self.tree_n = len(arr_list) if type(arr_list) == list else arr_list
        self.arr_list = arr_list if type(arr_list) == list else range(self.tree_n)
        self.reverse = False

    def _combine_tree(self, root, rest, depth):
        """生成树函数 """
        depth += 1
        if depth <= self.tree_q:
            for each in rest:
                next_rest = copy.deepcopy(rest)
                next_root = root + [each]
                next_rest.remove(each)
                self._combine_tree(next_root, next_rest, depth)
        else:
            root = sorted(root)
            if root not in self.tree_combine_List:
                self.tree_combine_List.append(root)

    def cnm(self, m=0):
        """C N 取 M 个的组合 """
        if m > math.floor(len(self.arr_list) / 2):
            m = len(self.arr_list) - m
            self.reverse = True
        self.tree_q = m
        self._combine_tree([], self.arr_list, 0)
        if self.reverse:
            self.tree_combine_List = map(lambda x: list(set(self.arr_list).difference(set(x))), self.tree_combine_List)
        return self.tree_combine_List

    def create_tree(self):
        """生成组合 """
        for each in range(1, self.tree_n + 1):
            self.tree_q = each
            self._combine_tree([], self.arr_list, 0)
        return self.tree_combine_List
