# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""
Usage Of 'chainmap' :
"""

try:
    from collections import ChainMap
except ImportError:
    from lgblearn.compat.chainmap_impl import ChainMap


class DeepChainMap(ChainMap):

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

    # override because the m parameter is introduced in Python 3.4
    def new_child(self, m=None):
        if m is None:
            m = {}
        return self.__class__(m, *self.maps)
