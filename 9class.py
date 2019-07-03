# -*- coding: utf-8 -*-


# 定义Person类
class Person(object):
    """
    类的文档字符串，对类的描述信息
    """
    # __method__(self) magic method 魔术方法

    # 构造函数，构造器，在创建对象时自动调用
    def __init__(self, xname, xage, xweight):
        # print "init method called"
        self.name = xname
        self.age = xage
        self.weight = xweight
        return

    # 析构函数 在销毁对象时自动调用
    def __del__(self):
        print "del method called"

    # 定义在类中的函数: 类方法 (class method)
    def eat(self, food):
        print "%s在吃%s"%(self.name, food)


if __name__ == '__main__':
    print "before"
    p = Person('tom', 22, 88.78)
    print "after"



    # 方式1. 通过对象调用类方法: 对象.方法(...)
    p.eat('饺子')

    # 给对象属性name重新赋值
    p.name = '张三'
    p.eat('饺子')
    del p
    print "------------------"


