# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_8
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019-09-04
-------------------------------------------------
   Change Activity:  2019-09-04:
-------------------------------------------------
"""

'''
Reverse Integer
'''

'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
'''

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    str_x = str(x)
    x = ''
    if str_x[0] == '-':
        x += '-'
    x += str_x[len(str_x) - 1::-1].lstrip("0").rstrip("-")
    x = int(x)
    if -2 ** 31 < x < 2 ** 31 - 1:
        return x
    return 0

if __name__ == '__main__':


    num = reverse(1234567890)
    print num

    pass