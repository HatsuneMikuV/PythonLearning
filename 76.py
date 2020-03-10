# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        76
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/3/10
-------------------------------------------------
   Change Activity:  2020/3/10:
-------------------------------------------------
"""


'''
题目：使用lambda来创建匿名函数。
'''

MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x


if __name__ == '__main__':

    a = 10
    b = 20
    print 'The largar one is %d' % MAXIMUM(a,b)
    print 'The lower one is %d' % MINIMUM(a,b)

    pass