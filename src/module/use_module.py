#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""use module
Python module 教学示例：
- 作为模块导入时，可使用 show_args() 和 show_name()
- 直接执行时，打印 __name__ 和命令行参数
"""

__author__ = 'kai'

import sys

def show_name():
    """显示当前模块的 __name__。"""
    print('__name__:', __name__)


def show_args():
    """显示命令行参数。"""
    args = sys.argv
    print('命令行参数数量:', len(args))
    for index, arg in enumerate(args):
        print('-' * 10)
        print('arg[{}]: {}'.format(index, arg))
        print('-' * 10)


if __name__ == '__main__':
    print('直接执行脚本时 __name__ 的值:', __name__)
    show_args()

if __name__ != '__main__':
    print('模块导入时 __name__ 的值:', __name__)




    

