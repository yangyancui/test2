# -*- coding: utf-8 -*-

import sys
import random

if __name__ == '__main__':
    sys.path.append(r'D:\tmp')
    import foo
    # sys.path 模块搜索路径(使用import导入python文件或包时，去哪些目录下查找这些模块或包),路径列表
    print sys.path
    for p in sys.path:
        print p


