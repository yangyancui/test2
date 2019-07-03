# -*- coding: utf-8 -*-


# 定义Person类
class Person(object):
    """
    类的文档字符串，对类的描述信息
    """

    count = 0

    def __init__(self, xname, xage, xweight):
        # print "init method called"
        self.name = xname
        self.age = xage
        self.weight = xweight
        Person.count += 1
        return

    # >
    def __gt__(self, other):
        # print "gt method called"
        return self.age > other.age

    # >=
    def __ge__(self, other):
        # print "ge method called"
        return self.age >= other.age
        # return 'hello'

    def __del__(self):
        self.__class__.count -= 1

    # 定义在类中的函数: 类方法 (class method)
    def eat(self, food):
        print "%s在吃%s"%(self.name, food)

    @property # 把类方法变成一个当前对象的属性，返回值就是属性的值
    def xusui(self):
        return self.age + 1

if __name__ == '__main__':
    p1 = Person('tom', 42, 88.78)
    p2 = Person('jack', 24, 78.78)

    # 比较两个对象会调用相关的魔术方法  __gt__()  __ge__()
    # print p1 > p2
    # print p1 >= p2

    # print "p1对象的名字:%s,虚岁:%d"%(p1.name, p1.xusui())
    print "p1对象的名字:%s,虚岁:%d"%(p1.name, p1.xusui)

