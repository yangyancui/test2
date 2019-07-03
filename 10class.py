# -*- coding: utf-8 -*-


# 定义Person类
class Person(object):
    """
    类的文档字符串，对类的描述信息
    """
    # 类变量
    count = 0

    # 构造函数，构造器，在创建对象时自动调用
    def __init__(self, xname, xage, xweight):
        # print "init method called"
        self.name = xname
        self.age = xage
        self.weight = xweight
        Person.count += 1
        return

    # 析构函数 在销毁对象时自动调用
    def __del__(self):
        # print "del method called"
        self.__class__.count -= 1
        # Person.count -= 1

    # 定义在类中的函数: 类方法 (class method)
    def eat(self, food):
        print "%s在吃%s"%(self.name, food)


if __name__ == '__main__':
    p1 = Person('tom', 22, 88.78)
    p2 = Person('jack', 24, 88.78)
    # print "当前Person实例的数目:", p1.count
    print "当前Person实例的数目:", Person.count
    p3 = Person('mary', 24, 88.78)
    print "当前Person实例的数目:", Person.count
    del p1
    print "当前Person实例的数目:", Person.count


