# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        52
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/7
-------------------------------------------------
   Change Activity:  2020/1/7:
-------------------------------------------------
"""

'''
题目：求1+2!+3!+...+20!的和。
'''

import math

def factorialTotal(number):
    res = 0
    an = 1
    for n in range(1, number + 1):
        an *= n
        res += an
    return res

if __name__ == '__main__':

    print factorialTotal(20)

    pass

