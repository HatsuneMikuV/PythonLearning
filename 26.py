# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        26
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/9/19
-------------------------------------------------
   Change Activity:  2019/9/19:
-------------------------------------------------
"""

# 1-3+5-7+...-(num-2) + num
def one_match(num):
    sub = False
    result = 0
    start = 1
    while start <= num:
        if sub:
            result -= start
        else:
            result += start
        start += 2
        sub = (sub == False)
    return result

# 1000-2000
def two_match(first, last):
    row = 0
    result = ''
    while first <= last:
        if first % 400 == 0 or first % 4 == 0:
            if row % 3 == 0:
                row = 0
                result += '\n'
            row += 1
            result = result + ' ' + str(first)
        first += 1
    return result

#
def mult_num(num):
    one = 1
    result = 1
    while one <= num:
        result *= one
        one += 1
    return result

def three_match(num):
    one = 1
    result = 0
    while one <= num:
        result = result + mult_num(one)
        one += 2
    return result


def four_match(first, last):
    result = []
    for i in range(first, last):
        j = 2
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result

import time
import dateutil
import datetime

if __name__ == '__main__':

    # print one_match(101)
    # print two_match(1000, 2000)
    # print three_match(9)
    # print four_match(200, 300)

    pass
