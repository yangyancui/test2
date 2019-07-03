# -*- coding: utf-8 -*-


import os


if __name__ == '__main__':


    try:
        print "--- try start ---"
        a = 3 / 1
        print "--- try end ---"
    except: # 当try代码块产生异常，立即执行except代码块处理异常
        print "异常产生了"

    print "程序正常结束"