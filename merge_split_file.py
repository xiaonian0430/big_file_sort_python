# encoding: utf-8
"""
@author: xiao nian
@contact: xiaonian030@163.com
@date: 2024-01-21
"""
__copyright__ = "Copyright (c) (2022-2024) XN Inc. All Rights Reserved"
__author__ = "Xiao Nian"
__version__ = "1.0.0"

import os
import math


def merge(file_list):
    file_handle_list = [open(file_, 'r') for file_ in file_list]
    temp_dict = {}
    merged_file = open('data/big_file_sorted.txt', 'a')
    for file_handle in file_handle_list:
        line_data = file_handle.readline()
        if line_data:
            temp_dict[file_handle] = line_data
    while temp_dict:
        min_item = min(temp_dict.items(), key=lambda x: x[1])
        merged_file.write(min_item[1])
        next_line = min_item[0].readline()
        if next_line:
            temp_dict[min_item[0]] = next_line
        else:
            del temp_dict[min_item[0]]
            min_item[0].close()
    merged_file.close()


if __name__ == '__main__':
    file_list = ['data\\split_1', 'data\\split_2', 'data\\split_3', 'data\\split_4', 'data\\split_5']

    merge(file_list)
