# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        75
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/21
-------------------------------------------------
   Change Activity:  2020/1/21:
-------------------------------------------------
"""
'''
题目：数字比较。
'''

def comparenum(a, b):

    if a == b:
        print '%d == %d' % (a, b)
    elif a > b:
        print '%d > %d' % (a, b)
    else:
        print '%d < %d' % (a, b)


if __name__ == '__main__':

    comparenum(3, 5)
    comparenum(5, 3)
    comparenum(3, 3)

    pass