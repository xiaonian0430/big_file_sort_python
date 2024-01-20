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


def split(path, chunk):
    """
    文件分割
    :param path: 大文件路径
    :param chunk: 分割文件大小限制，例如200*1024*1024/10
    :return: 分割后的文件列表
    """
    base_dir, base_file = os.path.split(path)
    file_index = 1
    file_list = []
    with open(path, 'r') as file_handle:
        while True:
            line_data_list = file_handle.readlines(chunk)
            if line_data_list:
                # 先排序，在写入新的文件
                line_data_list.sort()
                file_split = os.path.join(base_dir, 'split_' + str(file_index))
                with open(file_split, 'a') as split_handle:
                    split_handle.write(''.join(line_data_list))
                file_list.append(file_split)
                file_index += 1
            else:
                break
    return file_list


if __name__ == '__main__':
    big_file = 'data/big_file.txt'

    # 拆分成200M的文件大小
    size = math.floor(200 * 1024 * 1024)
    files = split(big_file, size)
    print(files)
