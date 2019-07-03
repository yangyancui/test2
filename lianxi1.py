# -*- coding: utf-8 -*-

# 输入年月日，判断该日期是这一年的第几天

# 31day  1 3 5 7 8 10 12
# 30day  4 6 9 11
# 2月 闰年 29天 平年 28天




if __name__ == '__main__':
    year = input('请输入年:')
    month = input('请输入月:')
    day = input('请输入日:')


    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 如果是闰年，2月天数是29
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        months[1] = 29

    days = 0
    for i in range(month - 1):
        days += months[i]

    days += day

    print "该日期是这一年的第%d天"%days
