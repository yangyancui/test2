# -*- coding: utf-8 -*-


import sys
import os


if __name__ == '__main__':
    # 当前进程的参数列表
    # print sys.argv

    sys.argv.pop(0)
    for arg in sys.argv:
        os.mkdir(arg)

    # sys.exit() 结束当前进程
    # sys.exit('hahaha')
    # sys.exit(1)

    # 正常结束
    sys.exit(0)

    print "this won't be printed"