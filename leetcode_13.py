# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:        leetcode_13
   Description :     ^_^ !!!
   Author :          anglemiku
   Eamil :           anglemiku.v@gmail.com
   date:             2019/12/28
-------------------------------------------------
   Change Activity:  2019/12/28:
-------------------------------------------------
"""

'''
Integer to Roman
'''

'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

'''

def Integer_to_Roman(number):

    if number >= 1000:
        res = (number / 1000) * "M"
        return res + Integer_to_Roman(number % 1000)

    if number >= 900:
        return "CM" + Integer_to_Roman(number - 900)

    if number >= 500:
        res = "D" + (number - 500) / 100 * "C"
        return res + Integer_to_Roman(number % 100)

    if number >= 400:
        return "CD" + Integer_to_Roman(number - 400)

    if number >= 100:
        res = (number / 100) * "C"
        return res + Integer_to_Roman(number % 100)

    if number >= 90:
        return "XC" + Integer_to_Roman(number - 90)

    if number >= 50:
        res = "L" + (number - 50) / 10 * "X"
        return res + Integer_to_Roman(number % 10)

    if number >= 40:
        return "XL" + Integer_to_Roman(number - 40)

    if number >= 10:
        res = (number / 10) * "X"
        return res + Integer_to_Roman(number % 10)

    if number >= 9:
        return "IX" + Integer_to_Roman(number - 9)

    if number >= 5:
        return "V" + (number - 5) * "I"

    if number >= 4:
        return "IV"

    return number * "I"

def intToRoman(num):
    num_dict = {1: 'I',
                4: 'IV',
                5: 'V',
                9: 'IX',
                10: 'X',
                40: 'XL',
                50: 'L',
                90: 'XC',
                100: 'C',
                400: 'CD',
                500: 'D',
                900: 'CM',
                1000: 'M'}
    res = ""
    for key in sorted(num_dict.keys())[::-1]:
        if num == 0:
            break
        tmp = num // key
        if tmp == 0:
            continue
        res += num_dict[key] * tmp
        num -= key * tmp
    return res

import time
if __name__ == '__main__':

    print time.time()
    print Integer_to_Roman(2994)
    print time.time()
    print intToRoman(2994)
    print time.time()

    pass