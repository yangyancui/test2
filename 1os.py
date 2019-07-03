# -*- coding: utf-8 -*-


import os


if __name__ == '__main__':

    # os.system() 执行系统命令,执行成功返回0
    # ret = os.system(r'md D:\aaa')
    # print ret

    # 列出目录下所有的文件名，返回列表类型
    print os.listdir(r'D:\tmp')

    # D:\tmp\abc\123.txt
    # /etc/httpd/conf/httpd.conf
    # 当前操作系统的路径分隔符
    print os.sep
    print r'abc\123.txt'
    print r'abc' + os.sep + r'123.txt'
    print r'abc%s123.txt'%os.sep

    # 环境变量Path的多个路径之间的分割符
    print os.pathsep

    # 当前目录
    print os.curdir
    # 当前目录的上一级目录
    print os.pardir

    file = r'D:\tmp\abc\test'
    print os.path.dirname(file)
    print os.path.basename(file)