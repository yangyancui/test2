# -*- coding: utf-8 -*-


# 定义一个银行帐户的类 Account
# 名字 name 卡号 cardno  余额 balance
# 取钱withdraw() 存钱deposit()  查询余额 check()



class Account:
    """
    描述银行帐户
    """

    def __init__(self, name, cardno, balance):
        self.name = name
        self.cardno = cardno
        self.balance = balance
        return


    def withdraw(self, amount):
        """
        取钱
        :param amount:
        :return: 成功返回0，余额不足返回1，参数非法返回2
        """
        if amount <= 0:
            return 2
        elif amount > self.balance:
            return 1
        else:
            self.balance -= amount
            return 0


    def deposit(self, amount):
        """
        存钱
        :param amount:
        :return: 存钱成功返回0，失败返回-1
        """
        if amount > 0:
            self.balance += amount
            return 0
        return -1


    def check(self):
        """
        查询余额
        :return:
        """
        return self.balance

    @property
    def money(self):
        """
        查询余额
        :return:
        """
        return self.balance


if __name__ == '__main__':
    a = Account('jack', '11223344', 1000)
    print "当前帐户余额:",a.check()
    a.deposit(500)
    print "当前帐户余额:", a.check()
    ret = a.withdraw(800)
    if ret != 0:
        print "取钱失败"
    print "当前帐户余额:", a.money