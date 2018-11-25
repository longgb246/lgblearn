# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/25
"""  
Usage Of '_version' : 
"""

import sys
import platform

# the version of python
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] >= 3
PY35 = sys.version_info >= (3, 5)
PY36 = sys.version_info >= (3, 6)
PY37 = sys.version_info >= (3, 7)
PYPY = platform.python_implementation() == 'PyPy'

# the version of platform
PMAC = any(list(map(lambda x: x in platform.system().lower(), ('darwin', 'os2', 'os', 'mac'))))
PWIN = any(list(map(lambda x: x in platform.system().lower(), ('win32', 'cygwin', 'win'))))
