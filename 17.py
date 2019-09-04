# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     seventeen
   Description :
   Author :       joe
   date：          2019-08-14
-------------------------------------------------
   Change Activity:
                   2019-08-14:
-------------------------------------------------
"""

import os

'''
Python 异常处理
python提供了两个非常重要的功能来处理python程序在运行中出现的异常和错误。你可以使用该功能来调试python程序。

异常处理: 本站Python教程会具体介绍
'''


'''
python标准异常
异常名称	                    描述
BaseException	            所有异常的基类
SystemExit	                解释器请求退出
KeyboardInterrupt	        用户中断执行(通常是输入^C)
Exception	                常规错误的基类
StopIteration	            迭代器没有更多的值
GeneratorExit	            生成器(generator)发生异常来通知退出
StandardError	            所有的内建标准异常的基类
ArithmeticError	            所有数值计算错误的基类
FloatingPointError	        浮点计算错误
OverflowError	            数值运算超出最大限制
ZeroDivisionError	        除(或取模)零 (所有数据类型)
AssertionError	            断言语句失败
AttributeError	            对象没有这个属性
EOFError	                没有内建输入,到达EOF 标记
EnvironmentError	        操作系统错误的基类
IOError	                    输入/输出操作失败
OSError	                    操作系统错误
WindowsError	            系统调用失败
ImportError	                导入模块/对象失败
LookupError	                无效数据查询的基类
IndexError	                序列中没有此索引(index)
KeyError	                映射中没有这个键
MemoryError	                内存溢出错误(对于Python 解释器不是致命的)
NameError	                未声明/初始化对象 (没有属性)
UnboundLocalError	        访问未初始化的本地变量
ReferenceError	            弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	            一般的运行时错误
NotImplementedError	        尚未实现的方法
SyntaxError	Python          语法错误
IndentationError	        缩进错误
TabError	                Tab 和空格混用
SystemError	                一般的解释器系统错误
TypeError	                对类型无效的操作
ValueError	                传入无效的参数
UnicodeError	            Unicode 相关的错误
UnicodeDecodeError	        Unicode 解码时的错误
UnicodeEncodeError	        Unicode 编码时错误
UnicodeTranslateError	    Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	        关于被弃用的特征的警告
FutureWarning	            关于构造将来语义会有改变的警告
OverflowWarning	            旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	            可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	            可疑的语法的警告
UserWarning	                用户代码生成的警告
'''

'''
什么是异常？
异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。

一般情况下，在Python无法正常处理程序时就会发生一个异常。

异常是Python对象，表示一个错误。

当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。

异常处理
捕捉异常可以使用try/except语句。

try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理。

如果你不想在异常发生时结束你的程序，只需在try里捕获它。
'''


def test():
    try:
        fh = open("testfile", "w")
        fh.write("这是一个测试文件，用于测试异常!!")
    except IOError:
        print "Error: 没有找到文件或读取文件失败"
    else:
        print "内容写入文件成功"
        fh.close()

    os.remove('testfile')


'''
try-finally 语句
try-finally 语句无论是否发生异常都将执行最后的代码

异常的参数
一个异常可以带上参数，可作为输出的异常信息参数。

你可以通过except语句来捕获异常的参数

'''

def temp_cpnver(var):
    try:
        return int(var)
    except ValueError, error:
        print 'var is not have num: ', error


'''
触发异常
我们可以使用raise语句自己触发异常

raise语法格式如下：
'''

def funcname(level):
    if level < 1:
        raise Exception('Invalid level', level)



'''
用户自定义异常
通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。

以下为与RuntimeError相关的实例,实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。

在try语句块中，用户自定义的异常后执行except块语句，变量 e 是用于创建Networkerror类的实例
'''

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


if __name__ == '__main__':

    test()

    temp_cpnver('yy1')

    funcname(1)

    try:
        raise Networkerror("Bad hostname")
    except Networkerror, e:
        print e.args

    pass