# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     four
   Description :
   Author :       joe
   date：          2019-07-18
-------------------------------------------------
   Change Activity:
                   2019-07-18:
-------------------------------------------------
"""
#
# Python 变量类型
# 变量存储在内存中的值。这就意味着在创建变量时会在内存中开辟一个空间。
#
# 基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
#
# 因此，变量可以指定不同的数据类型，这些变量可以存储整数，小数或字符。


# 变量赋值
# Python 中的变量赋值不需要类型声明。
#
# 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
#
# 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#
# 等号（=）用来给变量赋值。
#
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：


counter = 100   # 赋值整型变量
miles = 100.0  # 赋值浮点型
name = "Joe"  # 字符串

print(counter, miles, name)


# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：

a = b = c = d = 1
print(a, b, c, d)

# 也可以为多个对象指定多个变量。例如：
a, b, c, d = 100, 100.0, 'Joe', "Joe"
print(a, b, c, d)


'''
标准数据类型

在内存中存储的数据可以有多种类型。
例如，一个人的年龄可以用数字来存储，他的名字可以用字符来存储。
Python 定义了一些标准类型，用于存储各种类型的数据。
Python有五个标准的数据类型：

    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Dictionary（字典）
'''

# Python数字
# Python支持四种不同的数字类型：
#
# int（有符号整型）
# long（长整型[也可以代表八进制和十六进制]）
# float（浮点型）
# complex（复数）

# 数字数据类型用于存储数值
# 是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象
# 当指定一个值时，Number对象就会被创建
var1 = 1
var2 = 10
print(var1, var2)

# 可以使用del语句删除一些对象的引用
del var1, var2
# print(var1, var2)  NameError: name 'var1' is not defined

'''
注意：long 类型只存在于 Python2.X 版本中，
在 2.2 以后的版本中，int 类型数据溢出后会自动转为long类型。
在 Python3.X 版本中 long 类型被移除，使用 int 替代。
'''

# Python字符串
# 字符串或串(String)是由数字、字母、下划线组成的一串字符。

# python的字串列表有2种取值顺序:
#
# 从左到右索引默认0开始的，最大范围是字符串长度少1
# 从右到左索引默认-1开始的，最大范围是字符串开头

s = "abcdefg"
#  0  1  2  3  4  5  6    从左往右
# -7 -6 -5 -4 -3 -2 -1    从右往左

# [头下标:尾下标] 获取的子字符串包含头下标的字符，但不包含尾下标的字符
s1 = s[1:5]

print(s, s1)

# 加号（+）是字符串连接运算符，星号（*）是重复操作

print(s)            # 输出完整字符串
print(s[0])         # 输出字符串中的第一个字符
print(s[2:5])       # 输出字符串中第三个至第六个之间的字符串
print(s[2:])        # 输出从第三个字符开始的字符串
print(s * 2)        # 输出字符串两次
print(s + "TEST")   # 输出连接的字符串


# Python 列表截取可以接收第三个参数，参数作用是截取的步长，
# 以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
letters = ["a", "b", "c", "d", "e", "f", "g"]
str1 = letters[1:6:2]
print(letters, str1)


# Python列表
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
# 列表用 [ ] 标识，是 python 最通用的复合数据类型
# 列表中值的切割也可以用到变量 [头下标:尾下标] ，切割规则同上字符串切割

list = ["123", "abc", 123, 'qwe', 123.0, 1000]
otherlist = ["number", 555]

print(list)             # 输出完整列表
print(list[0])          # 输出列表的第一个元素
print(list[1:4])        # 输出第二个至第4个元素
print(list[3:])         # 输出从第4个开始至列表末尾的所有元素
print(list[1:4:2])      # 输出从第2个开始至第4个元素，步长为2截取的list
print(otherlist * 2)    # 输出列表两次
print(otherlist + list) # 打印组合的列表

list[2] = 100001        # 数组是可更改元素
print(list)

# Python 元组
# 元组是另一个数据类型，类似于 List（列表）。
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。不可变数组？
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple                 # 输出完整元组
print tuple[0]              # 输出元组的第一个元素
print tuple[1:3]            # 输出第二个至第四个（不包含）的元素
print tuple[2:]             # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2         # 输出元组两次
print tuple + tinytuple     # 打印组合的元组

# tuple[2] = 1000
# 元组中是非法应用  TypeError: 'tuple' object does not support item assignment


# Python 字典
# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。
# 列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']           # 输出键为'one' 的值
print dict[2]               # 输出键为 2 的值
print tinydict              # 输出完整的字典
print tinydict.keys()       # 输出所有键
print tinydict.values()     # 输出所有值



# Python数据类型转换
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

'''
函数	                            描述
int(x [,base])                  将x转换为一个整数
long(x [,base] )                将x转换为一个长整数
float(x)                        将x转换到一个浮点数
complex(real [,imag])           创建一个复数
str(x)                          将对象 x 转换为字符串
repr(x)                         将对象 x 转换为表达式字符串
eval(str)                       用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                        将序列 s 转换为一个元组
list(s)                         将序列 s 转换为一个列表
set(s)                          转换为可变集合
dict(d)                         创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)                    转换为不可变集合
chr(x)                          将一个整数转换为一个字符
unichr(x)                       将一个整数转换为Unicode字符
ord(x)                          将一个字符转换为它的整数值
hex(x)                          将一个整数转换为一个十六进制字符串
oct(x)                          将一个整数转换为一个八进制字符串
'''



