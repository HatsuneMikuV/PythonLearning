# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        77
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/3/10
-------------------------------------------------
   Change Activity:  2020/3/10:
-------------------------------------------------
"""

'''
题目：输出一个随机数。
'''

import random

if __name__ == '__main__':

    print "0 ~ 1 之间的随机数", random.random()
    print "0 ~ 100 之间随机整数 ", random.randint(0, 101)
    print "0 ~ 100 之间随机浮点数 ", random.uniform(0, 101)
    print "0 ~ 99间的随机数", random.choice([x for x in range(0, 100)])

    pass