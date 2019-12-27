# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        45
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/27
-------------------------------------------------
   Change Activity:  2019/12/27:
-------------------------------------------------
"""

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

'''
程序分析：关键是计算出每一项的值。

1，可以直接利用string的特性 将数字字符串直接 * n 得到每一项数字字符串，然后转int相加

2，采用累加得到每一项的值，然后相加
'''


if __name__ == '__main__':
    n = int(raw_input('n = '))
    a = raw_input('a = ')

    Sn = 0
    for index in range(1, n + 1):
        ss = a * index
        print ss
        Sn += int(ss)

    print "1, 计算和为：", Sn

    Sn = 0
    An = 0
    s = int(a)
    for i in range(n):
        An += s
        s *= 10
        Sn += An
        print An
    print "2, 计算和为：", Sn
    pass