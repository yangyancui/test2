# --*-- encoding:utf-8 --*--
class Account(object):
    """
    描述银行账户
    """
    def __init__(self,name,cardno,balance):
        self.name = name
        self.cardno = cardno
        self.balance = balance
        return
    def greet(self):
        print "欢迎你取钱，尊贵的客户"

    def greet1(self):
        print "欢迎你存钱，尊贵的客户"

    def withdraw(self,amount):
        """
        取钱
        :param amount:
        :return: 成功返回0，余额不足返回1，参数非法返回2
        """
        self.greet()
        if amount <= 0:
            return 2
        elif amount > self.balance:
            return 1
        else:
            self.balance -= amount
            return 0
    def deposit(self,amount):
        """
        存钱
        :param amount:
        :return:存钱成功返回0，失败返回-1
        """
        self.greet1()
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

if __name__ == '__main__':
    a = Account('jack','4567',1000)
    print "当前账户余额",a.check()
    # a.withdraw(300)
    # print "取钱成功",a.check()
    a.deposit(500)
    print "存钱成功",a.check()
