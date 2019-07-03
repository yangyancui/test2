# -*- coding: utf-8 -*-


import os


if __name__ == '__main__':


    try:
        print "--- try start ---"
        # a = 3 / 0
        # open(r'D:\111.txt')
        print "--- try end ---"
    except IOError: # 当try代码块产生IOError异常,执行except代码块
        print "IOError异常产生了"
    except ZeroDivisionError:
        print "ZeroDivisionError异常产生了"
    finally: # 不管是否try代码块抛出异常，都会执行finally代码块
        print "我一定会被执行"


    print "程序正常结束"