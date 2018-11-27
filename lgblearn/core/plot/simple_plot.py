# -*- coding:utf-8 -*-
# @Author  : 'longguangbin'
# @Contact : lgb453476610@163.com
# @Date    : 2018/11/27
"""  
Usage Of 'simple_plot' : 
"""

from plot_components import *


def barplot(y, x, figsize=(10, 7), ax=None, log=False, xlabel='', ylabel='', title='', width=0.6, color=None, **kwargs):
    """bar plot

    :param y:
    :param x:
    :param figsize:
    :param ax:
    :param bool log: log the data
    :param xlabel:
    :param ylabel:
    :param title:
    :param width: the width of the bar, default 0.6
    :param color: color list, default dark_colors
    :param kwargs:
    :return:
    """
    if not ax:
        fig = plt.figure(figsize=figsize)
        ax = fig.add_subplot(111)

    x_org = x
    if log:
        x = np.log10(x)
        _format = log_format
        ylabel += ' (log)'
    else:
        _format = normal_format

    color = color or dark_colors
    kwargs = dict({
        'width': width,
        'color': color,
    }, **kwargs)

    ax.bar(y, x, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)

    for p, x_i in zip(ax.patches, x_org):
        height = p.get_height()
        ax.text(p.get_x() + p.get_width() / 2., height + 0.02, str(x_i), ha="center", va='bottom')

    formatter = FuncFormatter(_format)
    ax.yaxis.set_major_formatter(formatter)

    return ax
