# encoding: utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-21
"""
__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__version__ = "1.0.0"

import random
import math


def create(file, lines):
    with open(file, 'a') as file_handle:
        for i in range(lines):
            # 换行符占用2个字节
            value = random.randint(10000000, 99999999)
            file_handle.write(str(value) + '\n')


if __name__ == '__main__':
    out_file = 'data/big_file.txt'
    lines = math.ceil(1024 * 1024 * 1024 / 10)
    create(out_file, lines)
    print('finish')
