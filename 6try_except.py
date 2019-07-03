# -*- coding: utf-8 -*-


import os


if __name__ == '__main__':


    # try:
    #     print "--- try start ---"
    #     # a = 3 / 0
    #     open(r'D:\111.txt')
    #     print "--- try end ---"
    # except IOError: # 当try代码块产生IOError异常,执行except代码块
    #     print "IOError异常产生了"
    # except ZeroDivisionError:
    #     print "ZeroDivisionError异常产生了"

    # try:
    #     print "--- try start ---"
    #     # a = 3 / 0
    #     # open(r'D:\111.txt')
    #     os.remove(r'D:\111.txt')
    #     print "--- try end ---"
    # except IOError: # 当try代码块产生IOError异常,执行except代码块
    #     print "IOError异常产生了"
    # except ZeroDivisionError:
    #     print "ZeroDivisionError异常产生了"
    # except:
    #     print "其他异常产生了"

    # try:
    #     print "--- try start ---"
    #     # a = 3 / 0
    #     # open(r'D:\111.txt')
    #     # os.remove(r'D:\111.txt')
    #     print "--- try end ---"
    # except IOError: # 当try代码块产生IOError异常,执行except代码块
    #     print "IOError异常产生了"
    # except ZeroDivisionError:
    #     print "ZeroDivisionError异常产生了"
    # except:
    #     print "其他异常产生了"
    # else: # 当try代码块没有产生异常，执行else代码块
    #     print "哈哈哈,没有产生异常"

    try:
        print "--- try start ---"
        a = 3 / 0
        # open(r'D:\tmp\test.txt').write('hello')

        print "--- try end ---"
    except IOError as msg: # 当try代码块产生IOError异常,执行except代码块
        print "IOError:%s"%msg
    except ZeroDivisionError, msg:
        print "ZeroDivisionError:%s"%msg

    print "程序正常结束"