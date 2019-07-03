# -*- coding: utf-8 -*-


# 定义Person类
class Person(object):
    """
    类的文档字符串，对类的描述信息
    """

    # 定义在类中的函数: 类方法 (class method)
    def eat(self, food):
        print "%s在吃:%s"%(self.name, food)


if __name__ == '__main__':
    # 创建类的实例(instance),也称为对象(object)
    p = Person()

    # 定义对象属性
    p.name = '张三'
    # 调用类方法的两种方式:

    # 方式1. 通过对象调用类方法: 对象.方法(...)
    p.eat('饺子')

    # 方式2. 类.方法(类的实例, ...)
    Person.eat(p, '面条')

    p1 = Person()
    p1.name = '李四'
    p1.eat('米饭')

    print type(p)
    print type(p1)

    # 访问类的文档字符串
    print Person.__doc__