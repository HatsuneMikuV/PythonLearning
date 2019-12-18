# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        39
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/18
-------------------------------------------------
   Change Activity:  2019/12/18:
-------------------------------------------------
"""

'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''

'''
程序分析：
判断素数的方法：
用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
'''

from math import sqrt
def count_prime_number(left, right):
    result = []
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

    res = count_prime_number(101, 200)
    print res, len(res)
    pass