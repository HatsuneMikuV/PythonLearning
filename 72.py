# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        72
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/20
-------------------------------------------------
   Change Activity:  2020/1/20:
-------------------------------------------------
"""


'''
题目：统计 1 到 100 之和。
'''

def total(num):
    if num <= 0:
        return 0
    return num + total(num - 1)

def total_num(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res

if __name__ == '__main__':

    print total(100)
    print total_num(100)

    pass