# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        63
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2020/1/14
-------------------------------------------------
   Change Activity:  2020/1/14:
-------------------------------------------------
"""

'''
题目：求100之内的素数。(39.py)
'''

from math import sqrt
def count_prime_number(left, right):
    result = []
    if left < 2:
        left = 2
    for number in range(left, right + 1):
        k = int(sqrt(number + 1))
        leap = 0
        for index in range(2, k + 1):
            if number % index == 0:
                leap = 1
                break
        if leap == 0:
            result.append(number)
    return result


if __name__ == '__main__':

    print count_prime_number(1, 100)

    pass