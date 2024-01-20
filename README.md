# 大文件排序

大文件就是无法一次性全部读到内存中的文件。

为了操作不真的把我机器的内存都榨干，这里假设机器的内存是300MB，刨除一些系统占用，规定每次读到内存的文件大小不能超过200MB。

用下面的程序创建了一个1GB大小的测试文件

create_test_data.py
```python
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

```

这个文件一共有1024*1024*1024/10行，每一行以字符串格式存储着一位8位数，并在末尾加上了换行符（2个字节），所以每行占据10Byte，算下来一共有1024*1024*1024Byte也就是1GB。

下面要实现的就是在内存占用每次不超过200MB的情况下将这个1GB的文件进行排序。硬盘空间很大，随意使用。


## 大文件排序算法的思路

### 步骤一文件分割
首先来对文件进行分割，每次从原文件读200MB的整行数，然后保存到一个新文件。

```python
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

```

查看一下每个文件的大小，除了最后一个文件，其余的都是大约200MB

### 步骤二文件归并

需要将这些已排序的小文件按照归并法合并成新的大文件，该新文件就是已排序的大文件了。

