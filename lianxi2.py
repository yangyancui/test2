# -*- coding: utf-8 -*-


# 编写一个猜数字的游戏


import random

if __name__ == '__main__':

    r = random.randint(1, 100)

    while True:
        try:
            n = input("请猜一个数字[1--100]:")
            if n > r:
                print "猜大了"
            elif n < r:
                print "猜小了"
            else:
                break
        except: pass


    print "恭喜你，猜对啦"
