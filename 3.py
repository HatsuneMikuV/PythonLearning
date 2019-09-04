# -*- coding: utf-8 -*-

# Python 基础语法

# Python 语言与 Perl，C 和 Java 等语言有许多相似之处。但是，也存在一些差异。
#
# 在本章中我们将来学习 Python 的基础语法，让你快速学会 Python 编程。

# Python  基础

# 在 Python 里，标识符由字母、数字、下划线组成。
#
# 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
#
# Python 中的标识符是区分大小写的。
#
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，
# 需通过类提供的接口进行访问，不能用 from xxx import * 而导入。
#
# 以双下划线开头的 __foo 代表类的私有成员，以双下划线开头和结尾的 __foo__ 代表
# Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。


# Python 可以同一行显示多条语句，方法是用分号 ; 分开

print("hello,"); print("python!")


# Python 保留字符

# 下面的列表显示了在Python中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。
#
# 所有 Python 的关键字只包含小写字母。
# and	        exec	        not
# assert	    finally	        or
# break	        for	            pass
# class	        from	        print
# continue	    global	        raise
# def	        if	            return
# del	        import	        try
# elif	        in	            while
# else	        is	            with
# except	    lambda	        yield


# 行和缩进
# 学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
#
# 缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。

if True:
    print "True"
else:
    print "False"


# 多行语句
# Python语句中一般以新行作为语句的结束符。
#
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示, 如下所示：

item_one = 1
item_two = 10
item_three = 100

total = item_one + \
        item_two + \
        item_three

print(total)

# 语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：

days = ['Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday']

print(days)

# Python注释
# python中单行注释采用 # 开头。

'''
多行注释
多行注释
多行注释
'''


# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,


x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print("----------------")

# 不换行输出
print(x, y)

print x,
print y,
