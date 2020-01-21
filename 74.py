# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        74
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/21
-------------------------------------------------
   Change Activity:  2020/1/21:
-------------------------------------------------
"""
'''
题目：两个变量值互换。
'''

def exchange(a, b):
    return (b, a)

if __name__ == '__main__':

    a, b = 1, 2
    print a, b
    a, b = exchange(a, b)
    print a, b

    pass